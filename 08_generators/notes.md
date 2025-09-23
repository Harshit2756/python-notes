yield => pauses the function saving its state and allows it to be resumed later
next() => resumes the function from its last paused state
send(value) => resumes the function and sends a value that becomes the result of the last yield expression
throw(exception) => resumes the function and raises an exception at the point of the last yield expression
from => used to delegate part of a generator's operations to another generator
close() => terminates the generator, raising a GeneratorExit exception at the point of the last yield expression