
###################################RAG using vector db in phidata



from dotenv import load_dotenv  # Import load_dotenv
import os
import openai
from phi.agent import Agent
from phi.model.openai import OpenAIChat
from phi.embedder.openai import OpenAIEmbedder
from phi.knowledge.pdf import PDFUrlKnowledgeBase
from phi.vectordb.lancedb import LanceDb, SearchType

# Load environment variables from .env file
load_dotenv()

# Access API key from environment variable
api_key = os.getenv("OPENAI_API_KEY")

# Verify that the API key is loaded
if not api_key:
    raise ValueError("OPENAI_API_KEY is not set. Please check your .env file.")

# Create a knowledge base from a PDF
knowledge_base = PDFUrlKnowledgeBase(
    urls=["https://phi-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
    # Use LanceDB as the vector database
    vector_db=LanceDb(
        table_name="recipes",
        uri="tmp/lancedb",
        search_type=SearchType.vector,
        embedder=OpenAIEmbedder(model="text-embedding-3-small"),
    ),
)

# Comment out after first run as the knowledge base is loaded
knowledge_base.load(recreate=False)

agent = Agent(
    model=OpenAIChat(id="gpt-4o", api_key=api_key),
    # Add the knowledge base to the agent
    knowledge=knowledge_base,
    show_tool_calls=True,
    markdown=True,
)

# Make a query to the agent
agent.print_response("How do I make chicken and galangal in coconut milk soup", stream=True)




############################book recomendation agent
# from phi.agent import Agent
# from phi.model.openai import OpenAIChat
# from phi.tools.exa import ExaTools
# from dotenv import load_dotenv  # Import load_dotenv
# import os
# load_dotenv()

# # # Access API key from environment variable
# api_key = os.getenv("OPENAI_API_KEY")
# agent = Agent(
#     description="you help user with book recommendations",
#     name="Shelfie",
#     model=OpenAIChat(id="gpt-4o"),
#     instructions=[
#         "You are a highly knowledgeable book recommendation agent.",
#         "Your goal is to help the user discover books based on their preferences, reading history, and interests.",
#         "If the user mentions a specific genre, suggest books that span both classics and modern hits.",
#         "When the user mentions an author, recommend similar authors or series they may enjoy.",
#         "Highlight notable accomplishments of the book, such as awards, best-seller status, or critical acclaim.",
#         "Provide a short summary or teaser for each book recommended.",
#         "Offer up to 5 book recommendations for each request, ensuring they are diverse and relevant.",
#         "Leverage online resources like Goodreads, StoryGraph, and LibraryThing for accurate and varied suggestions.",
#         "Focus on being concise, relevant, and thoughtful in your recommendations.",
#     ],
#     tools=[ExaTools()],
# )
# agent.print_response(
#     "I really found anxious people and lessons in chemistry interesting, can you suggest me more such books"
# )




##############image description
# import os
# from dotenv import load_dotenv 
# from phi.agent import Agent
# from phi.model.openai import OpenAIChat
# load_dotenv()

# # # Access API key from environment variable
# api_key = os.getenv("OPENAI_API_KEY")
# agent = Agent(
#     model=OpenAIChat(id="gpt-4o"),
#     markdown=True,
# )

# agent.print_response(
#     "What are in these images? Is there any difference between them?",
#     images=[
#         "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
#         "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
#     ],
# )
