#!restMicroservice/bin/python

if __name__ == "__main__":
    dico_langues = {
    "C": 6, 
    "C#": 4, 
    "CSS": 1, 
    "Dart": 1, 
    "Go": 6, 
    "HTML": 1, 
    "Haskell": 1, 
    "Java": 1, 
    "JavaScript": 10, 
    "Jupyter Notebook": 3, 
    "Kotlin": 3, 
    "Objective-C": 1, 
    "PHP": 3, 
    "Python": 22, 
    "R": 1, 
    "Rust": 3, 
    "Shell": 4, 
    "Swift": 6, 
    "TeX": 1, 
    "TypeScript": 3, 
    "Vue": 1
    }
    d_sorted = sorted(dico_langues.items(), reverse=True, key=lambda x: x[1])
    languages_occurence = {i[0]: i[1] for i in d_sorted}
    print(languages_occurence)