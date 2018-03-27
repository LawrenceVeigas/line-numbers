# Resolving the line number issue at my work place

I'm Lawrence Veigas and I'm a Content Development Editor. Very recently I've been working on a book with some really amazing authors. However, with really amazing authors there are also challenges (opportunities in disguise) which help make content better for the readers.

To give you a general idea, the platform on which I work does not support number line in code blocks. So a basic code block looks like this:
```
  if (isAwesome){
    return true
  }
```
Naturally, the authors want to explain a particular line in the code so that the readers better understand what the author is talking about. Imagine a code block which is basically hundreds of lines of code. WE REQUIRE LINE NUMBERS! However, there are no line numbers supported on this platform (unlike GitHub). This is something which is in active development, however, we need to publish the book soon so we can't wait for this feature to get added.
So the editors (including me) started adding line numbers *manually* which was very frustrating and exhausting. That's when my programming senses kicked and I thought, let's write a small python script which will automate this task! And wola! That's what I've done and commited to this repository. So now, my code blocks look like this:
```
1  if (isAwesome){
2    return true
3  }
```
Additionally, I wrote some logic to handle the *indentation* bit too.

## Conclusion
This is a classic example where a little bit of hands-on experience in programming really help ease workflow and make life a bit easy.

### Moral of the story
Learn to code!
