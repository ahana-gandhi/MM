import scipy
import streamlit as st
import numpy as np
from transformers import AutoProcessor, MusicgenForConditionalGeneration

@st.cache_resource(show_spinner=False)
def generate_music(instrument, speed):

    processor = AutoProcessor.from_pretrained("facebook/musicgen-small")
    model = MusicgenForConditionalGeneration.from_pretrained("facebook/musicgen-small")

    inputs = processor(
        # text=["80s pop track with bassy drums and synth"],
        text=["soothing music with "+instrument+" at "+str(speed)+" beats per measure."],
        padding=True,
        return_tensors="pt",
    )

    # start = time.time()
    audio_values = model.generate(**inputs, max_new_tokens=500)
    # print(time.time() - start) # Log time taken in generation
    
    # Duplicate the audio 4 times to extend its length
    extended_audio = np.tile(audio_values[0, 0].numpy(), 5)

    sampling_rate = model.config.audio_encoder.sampling_rate
    scipy.io.wavfile.write("musicgen_out2.wav", rate=sampling_rate, data=extended_audio)
    
    return True
