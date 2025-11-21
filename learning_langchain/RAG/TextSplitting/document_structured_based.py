if __name__ == '__main__':
    from langchain.text_splitter import RecursiveCharacterTextSplitter, Language

    text = """
        class Employee:
        def __init__(self, name, age, tech_stack):
            self.name = name
            self.age = age
            self.tech_stack = tech_stack
    
        def display_details(self):
            print(f"Name: {self.name}")
            print(f"Age: {self.age}")
            # Handle the case where tech_stack is a list for better readability
            if isinstance(self.tech_stack, list):
                print(f"Tech Stack: {', '.join(self.tech_stack)}")
            else:
                print(f"Tech Stack: {self.tech_stack}")
    
        # Create an instance of the Employee class
        employee1 = Employee("Alice Smith", 30, ["Python", "Java", "SQL"])
        employee2 = Employee("Bob Johnson", 25, "JavaScript")
        
        # Display the details of the employees
        employee1.display_details()
        employee2.display_details()
    """

    splitter = RecursiveCharacterTextSplitter.from_language(
        language=Language.PYTHON,
        chunk_size=300,
        chunk_overlap=0
    )

    chunks = splitter.split_text(text)

    print(f'Chunks {chunks}\nLength of chunks is {len(chunks)}')