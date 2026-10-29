"""Office instances are private. Never close an existing user's application."""
import gc
import shutil
import tempfile
from pathlib import Path

def recalculate_xlsx(path):
    import pythoncom
    import win32com.client
    pythoncom.CoInitialize();app=book=None
    try:
        app=win32com.client.DispatchEx('Excel.Application')
        app.Visible=False;app.DisplayAlerts=False;app.AskToUpdateLinks=False;app.AutomationSecurity=3
        book=app.Workbooks.Open(str(Path(path).resolve()),UpdateLinks=0,ReadOnly=False)
        app.CalculateFullRebuild();book.Save()
    finally:
        if book is not None:book.Close(SaveChanges=False)
        book=None
        if app is not None:app.Quit()
        app=None;gc.collect();pythoncom.CoUninitialize()

def render_documents(folder):
    """Render short temporary copies; destination assignment names may be long."""
    import pythoncom
    import win32com.client
    import fitz
    pythoncom.CoInitialize();app=doc=None;results=[]
    folder=Path(folder);pdf_dir=folder/'Pratinjau_PDF';pdf_dir.mkdir(exist_ok=True)
    try:
        app=win32com.client.DispatchEx('Word.Application')
        app.Visible=False;app.DisplayAlerts=0;app.AutomationSecurity=3
        for i,f in enumerate(sorted(folder.glob('*.docx')),1):
            with tempfile.TemporaryDirectory(prefix='mpp-word-') as tmp:
                src=Path(tmp)/f'{i:02}.docx';dst=Path(tmp)/f'{i:02}.pdf';shutil.copy2(f,src)
                try:
                    doc=app.Documents.Open(str(src),False,True,False)
                    doc.Repaginate();doc.ExportAsFixedFormat(str(dst),17)
                    pages=int(doc.ComputeStatistics(2))
                finally:
                    if doc is not None:doc.Close(0)
                    doc=None
                target=pdf_dir/(f.stem+'.pdf');shutil.copy2(dst,target)
                errors=[]
                with fitz.open(dst) as pdf:
                    for n,p in enumerate(pdf,1):
                        for b in p.get_text('blocks'):
                            if b[0]<-1 or b[1]<-1 or b[2]>p.rect.width+1 or b[3]>p.rect.height+1:errors.append(f'Halaman {n}: teks di luar kertas')
                results.append({'file':f.name,'pages':pages,'layout_errors':errors})
    finally:
        if doc is not None:doc.Close(0)
        doc=None
        if app is not None:app.Quit(0)
        app=None;gc.collect();pythoncom.CoUninitialize()
    merged=fitz.open();toc=[];page=1
    for f in sorted(pdf_dir.glob('*.pdf')):
        with fitz.open(f) as d:
            toc.append([1,f.stem.replace('_',' '),page]);merged.insert_pdf(d);page+=len(d)
    # Include externally supplied PDFs in the preview without converting their signatures.
    for f in sorted(folder.glob('*.pdf')):
        if f.name=='Pratinjau_Seluruh_Dokumen.pdf':continue
        with fitz.open(f) as d:
            toc.append([1,f.stem.replace('_',' '),page]);merged.insert_pdf(d);page+=len(d)
    if len(merged):merged.set_toc(toc);merged.save(folder/'Pratinjau_Seluruh_Dokumen.pdf',garbage=4,deflate=True)
    merged.close();return results
