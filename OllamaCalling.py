import ollama

#initalie Ollama client
client = ollama.Client()

class OllamaCalling:
    #Define model and input prompt
    def __init__(self):
        self.model = "phi3:mini"
        #self.prompt = "For the following message, simply return the intent of the message (either events or weather) and any dates (if mentioned explicitly or implicitly in this format: Jan 20th) with a space between the two words (in this format: events May 30th): "
        #self.prompt = "Give the intent of a message (either return 'events' or 'weather') and the date, but only if it's explicitly mentioned (either as an actual date like 'May 27th' or relatively like 'today', 'tomorrow', or 'yesterday'). Do not give me any words, questions, statements, colons, equals, semi-colons, or filler in the message beyond the ones asked for. Put it all on one line in this format: 'weather today'. Here is the message you have to analyze: "
        #self.prompt = "You must respond with only the result in this exact format: "<intent> <date>" (e.g., "events May 27th" or "weather today"). - Only use 'events' or 'weather' for the intent. - Only include the date if explicitly mentioned as an actual date (e.g., 'May 27th') or as 'today', 'tomorrow', or 'yesterday'.- Do not add anything else: no explanations, colons, equals, punctuation, or extra words."
        self.prompt = "You must respond with only the result in this exact format: \"<intent> <date>\" (e.g., \"events May 27th\" or \"weather today\"). - Only use 'events' or 'weather' for the intent. - Only include the date if explicitly mentioned as an actual date (e.g., 'May 27th') or as 'today', 'tomorrow', or 'yesterday'.- Do not add anything else: no explanations, colons, equals, punctuation, or extra words,- Your message should not be capitalized. Here is the message: "


    #call this to get the variables
    def generate(self,text):
        self.prompt += text
        #print(self.prompt)
        
        #Send the query to the model
        response = client.generate(self.model,self.prompt)
        
        #print response
        print("Response from Ollama: ")
        print(response.response)

        return response.response

        