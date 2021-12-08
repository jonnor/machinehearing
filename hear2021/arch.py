
import yamnet
from yamnet import yamnet as yamnet_model
from yamnet import params

import openl3

#m = yamnet_model.yamnet_frames_model(params)

#print(m.summary())


m = openl3.models.load_audio_embedding_model(
            input_repr="mel256",
            content_type="music",
            embedding_size=512,
)


print(m.summary())
