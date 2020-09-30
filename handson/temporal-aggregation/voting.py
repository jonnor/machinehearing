import numpy
from sklearn.preprocessing import LabelBinarizer

labels = [ 'rock', 'jazz', 'blues', 'metal' ] 

binarizer = LabelBinarizer()
y = binarizer.fit_transform(labels)

print('labels\n', '\n'.join(labels))
print('y\n', y)

# Outputs from frame-based classifier. 
# input would be all the frames in one song
# frame_predictions = model.predict(frames)
frame_predictions = numpy.array([
    [ 0.5, 0.2, 0.3, 0.9 ],
    [ 0.9, 0.2, 0.3, 0.3 ],
    [ 0.5, 0.2, 0.3, 0.7 ],
    [ 0.1, 0.2, 0.3, 0.5 ],
    [ 0.9, 0.2, 0.3, 0.4 ],
])

def vote_majority(p):
    voted = numpy.bincount(numpy.argmax(p, axis=1))
    normalized = voted / p.shape[0]
    return normalized

def vote_average(p):
    return numpy.mean(p, axis=0)

def vote_average_logits(p):
    logits = numpy.log(p / (1 - p))
    avg = numpy.mean(logits, axis=1)
    p = 1/(1+ numpy.exp(-avg))
    return p


maj = vote_majority(frame_predictions)
mean = vote_average(frame_predictions)
mean_logits = vote_average_logits(frame_predictions)

genre_maj = binarizer.inverse_transform(numpy.array([maj]))
genre_mean = binarizer.inverse_transform(numpy.array([mean]))
genre_mean_logits = binarizer.inverse_transform(numpy.array([mean_logits]))
print('majority voting', maj, genre_maj)
print('mean voting', mean, genre_mean)
print('mean logits voting', mean_logits, genre_mean_logits)

