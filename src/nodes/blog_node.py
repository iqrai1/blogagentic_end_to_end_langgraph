from src.states.blogstate import BlogState
from langchain_core.messages import HumanMessage,SystemMessage
from src.states.blogstate import Blog

class BlogNode:
    """
    A class to represent the blog node
    """

    def __init__(self,llm):
        self.llm=llm

    def title_creation(self,state:BlogState):
        """
        Create the title for the blog
        """

        if "topic" in state and state["topic"]:
            prompt="""
                   You are an expert blog content writer. Use Markdown formatting. Generate
                   a blog title for the {topic}. This title should be creative and SEO friendly

                    """
            
            system_message = prompt.format(topic=state["topic"])
            print(system_message)
            response = self.llm.invoke(system_message)
            print(response)
            return {"blog":{"title":response.content}}
        
    def content_generation(self,state:BlogState):
        if "topic" in state and state["topic"]:
            system_prompt = """You are expert blog writer. Use Markdown formatting.
            Generate a detailed blog content with detailed breakdown for the {topic}"""
            
            system_message = system_prompt.format(topic=state["topic"])
            response = self.llm.invoke(system_message)
            return {"blog": {"title": state['blog']['title'], "content": response.content}}
        
    def translation(self,state:BlogState):
        """
        Translate the content to the specified language.
        """
        translation_prompt="""
        Translate the following content into {current_language}.
        - Maintain the original tone, style, and formatting.
        - Adapt cultural references and idioms to be appropriate for {current_language}.

        ORIGINAL CONTENT:
        {blog_content}

        """
        print(state["current_language"])
        blog_content=state["blog"]["content"]
        messages=[
            SystemMessage("You are an expert translator and content writer."),
            HumanMessage(translation_prompt.format(current_language=state["current_language"], blog_content=blog_content))

        ]
        transaltion_content = self.llm.with_structured_output(Blog).invoke(messages)
        return {"blog": {"content": transaltion_content}}

    def route(self, state: BlogState):
        return {"current_language": state['current_language'] }
    

    def route_decision(self, state: BlogState):
        if state["current_language"] == "urdu":
            return "urdu_translation"
        elif state["current_language"] == "french": 
            return "french_translation"
        else:
            return state['current_language']
