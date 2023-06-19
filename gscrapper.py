from flask import Flask,request,render_template
from requests_html import HTML
from requests_html import HTMLSession
import aspose.words as aw
gscrapper=Flask(__name__)#naming code
app=gscrapper
@app.route('/',methods=["GET"])#defining home route
def home():
    return render_template('index.html')

@app.route('/links',methods=['GET','POST'])#defining links route 
def reviews():
    if request.method=='POST':
        searchString = request.form['searchWordname'].replace(' ','')#getting search word from index.html
        searchString=searchString.replace(' ','')#removing the unwanted spaces
        google_base_url = "https://www.google.com/search?q="#google base url 
        google_search_url=google_base_url+searchString
        googleSearchLinks=[]#list for storing the dictionaries 
        #create document object
        doc = aw.Document()
        # create a document builder object
        builder = aw.DocumentBuilder(doc)
        try:
            google_html_request=HTMLSession().get(google_search_url)#getting page source
            websiteLinks=list(google_html_request.html.absolute_links)#separating the links
            try:
                for i in websiteLinks:
                    mydict={'search_word':searchString,
                    'website_link':i,
                    'goto_link':i}
                    googleSearchLinks.append(mydict)
                    builder.write(i)
                    builder.write('\n')
                # save document
                document_name=searchString+'.docx'
                doc.save(document_name)
            except:
                pass
        except :#handling exception
            pass
            
    return render_template('result.html',glinks=googleSearchLinks[0:(len(googleSearchLinks)-1)],document_name=document_name)#returning the result.html page

if __name__=='__main__':
    app.run(host='0.0.0.0',port=5000)