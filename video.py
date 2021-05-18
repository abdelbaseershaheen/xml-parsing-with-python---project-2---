import pandas as pd 
import xml.etree.ElementTree as ET
for i in range (10):
    try:
        filenamexml = "%s.xml" %i
        filenamecsv = "%s.csv" %i
        tree1 = ET.parse(filenamexml)
        root = tree1.getroot()
        data1 = []
        data2 = []
        for child in root.findall('./transcript/question[1]'):
            question_id = child.get('id')
            media_identifier = child.get('media_identifier')
            question_title = child.find('question_title').text
            for i in root.findall('./transcript/question[1]/p[1]/s[1]'):
                start_time = i.get('start_time')
                for i in root.findall('./transcript/question[1]/p[last()]/s[last()]'):
                    end_time = i.get('end_time')
                    data1.append(question_id)
                    data1.append(media_identifier)
                    data1.append(question_title)
                    data1.append(start_time)
                    data1.append(end_time)
            
            for l in root.findall('./transcript/question[2]'):
                question_id = l.get('id')
                media_identifier = l.get('media_identifier')
                question_title = l.find('question_title').text
                for i in root.findall('./transcript/question[2]/p[1]/s[1]'):
                    start_time = i.get('start_time')
                for i in root.findall('./transcript/question[2]/p[last()]/s[last()]'):
                    end_time = i.get('end_time')
                    data2.append(question_id)
                    data2.append(media_identifier)
                    data2.append(question_title)
                    data2.append(start_time)
                    data2.append(end_time)
    except:
        pass
     
        
            
data = [data1 , data2]
col = ['question_id', 'media_identifier' ,'question_title' ,'start_time' ,'end_time']
df = pd.DataFrame(data = data , columns = col)

df_transpose = df.T

df_transpose.to_csv(filenamecsv)