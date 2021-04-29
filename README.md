# nets213-final-project

Project: Translate for Tots

Translate for Tots will use crowdsourcing to help translate children’s songs and rhymes in a variety of languages. It solves the problem of children only having access to a limited number of children’s songs and rhymes in their native language. If more songs and rhymes are translated, young kids will have more options, which could also help grow their reading skills. 

There will be 2 groups in our crowd: one group that transcribes the children’s song or rhyme in its original language (language requirement would only have to be monolingual in the song/rhyme's language), and the other group would translate the text (bilingual requirement). The workers will provide either transcription or translation services, depending on their status as monolingual or multilingual. We will use quality checks and also have workers overlap on tasks and then compare and aggregate to find the most common answer to ensure correctness. We will also specifically have quality check tasks where we ask workers to determine if a translation or transcription is correct. Finally, we will combine the responses that have passed our quality checks mentioned previously. 

Step 0 (1 point): Select foreign language songs and rhymes. We are planning to get these from Mama Lisa’s World (International Music and Culture). 

Step 1 (3 points): Transcribe the children’s song/rhyme. This would be done by workers who are native speakers of the song/rhyme's original language. 

Step 2 (4 points): Transcription quality check. The transcription would then be checked for quality through automatic comparisons and aggregation through a different set of tasks done by workers who are fluent in the original language. 

Step 3 (2 points): Run transcription through Google Translate to get a rough transcription.

Step 4 (4 points): Workers then edit the Google Translate output for a more coherent translation.

Step 5 (4 points): Translation quality check. We finalize the translation through aggregation of worker responses. 

Step 6 (2 points): Reassemble the song/rhyme with the translations. 

## Data

For the “transcribe” part of this project, the format of our data will be in the form of images, with each image being a children’s rhyme or song. As stated, the data will be collected from the Mama Lisa’s World (International Music and Culture), available at https://www.mamalisa.com/?t=hubeh. Here, we will also include quality control checks to make sure workers are transcribing the images accurately. The first output from our workers will be the transcription of the words displayed on the page, which means it will be simple text. Samples of the images to be transcribed as well as the quality control checks can be found in the data/transcribe directory. The sample inputs are named in the form input_*, and the quality control inputs are named qc_input_*. The text files for which we will check the quality control HITs are labelled as qc_output_*_check, and correspond to the qc_input_* files.

Then, for the “translate” portion of this project, we will use Google Translate for the transcriptions, the output of which will be shown to the worker. The data passed into MTurk will consist of two parts for each HIT - a text file of the transcription (in the original language) and a text file of the translation (from Google Translate). The output here would be the edited translation that workers would write out as simple text. Quality control measures will be included here too, to make sure workers are not just randomly typing anything. Samples for all this data can be found in the data/translate directory. The transcription text files are named input_*_transcription, and the Google Translate translation text files are named input_*_translation. The quality control HITs are similarly named qc_input_*_transcription and qc_input_*_translation. The pre-annotated text files for these are named qc_output_*_check.

In both the "transcribe" and "translate" parts of this project, we want to keep one aggregated transcribed/translated version of the text. In order to choose one of these outputs given the multiple outputs we will get from each worker, we will use the quality control checks to create a "quality score" for each worker. Our similarity algorithm considers all specific details such as whether or not the worker included correct punctuations in the transcription as well. We will then choose the transcription/translation of the worker with the highest quality score. 

For the final version of our project, we will need to consider edge cases like when all the workers produce results with a very low similarity score to our quality check questions or in other words, have a low quality score. For the translation part of the algorithm, we could improve our final translation selection process. This is because when workers fix the translation from Google Translate, there are many more factors to consider other than whether it is similar to the quality check question. For example, some workers my word certain phrases differently for different contexts or style of writing. Therefore, taking translation from the worker with the highest quality score may not be best selection method in this case. 

The data folder contains all the raw images of the children's rhyme/song to be translated. 
The code the deals with the quality control and aggregation is located in the source folder in the files transcribe_qc_aggregation.py and translate_qc_aggregation.py. 
Sample outputs for the transcription and translation are also located in the source folder in the files sample_output_transcribe.csv and sample_output_translation.csv. 

## How To Contribute
Our project can be reached at this link: https://workersandbox.mturk.com/projects/30814BGWWGM42J1SX8Z2CTJJKDDH25/tasks?ref=w_pl_prvw.

1. Open the link to our MTurk project
2. The original nursery rhyme is put through Google Translate for a preliminary translation.
3. If you are bilingual (fluent in both English and the original language) you are qualified to complete translation tasks. 
4. A translation task involves making edits to the Google Translate version to fix any errors and make it more coherent. 
5. We will then run quality checks to choose the best translation. 
6. That’s it! Thank you for contributing to our project. 

If you have any questions, please contact: Riya Narayan (riyan@seas.upenn.edu)



