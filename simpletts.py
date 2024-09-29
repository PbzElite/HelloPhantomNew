from text_to_speech import save

text = "Hello"
language = "en"  # Specify the language (IETF language tag)
output_file = "output.mp3"  # Specify the output file (only accepts .mp3)

save(text, language, file=output_file)