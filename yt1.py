
from youtube_transcript_api import YouTubeTranscriptApi
import json 
from transformers import pipeline
from transformers import T5ForConditionalGeneration, T5Tokenizer


# define a variable to hold you app
# app = Flask(__name__)

# # define your resource endpoints
# app.route('/')
# def index_page():
#     return "Hello world"

# app.route('/time', methods=['GET'])
# def get_time():
#     return str(datetime.datetime.now())

# # server the app when this file is run
# if __name__ == '__main__':
#     app.run()

def summary_generator(vidId):
    videoId= vidId
    summary = (YouTubeTranscriptApi.get_transcript(videoId))
    value= [sub['text'] for sub in summary]
    #print(value)
    transc=""

    for i in summary:
         ( '[%s]' % ', '.join(map(str, value))) 
    summarization = pipeline ("summarization")
    summary_text = summarization(value)[0]['summary_text']
    print("Summary:", summary_text)
    
    
summary_generator("KuoHW5EiJdQ")







