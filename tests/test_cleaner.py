from app.ingestion.cleaner import clean_text

#1. for extra spaces and tabs
def test_remove_extra_spaces():
    result =clean_text("This is a test.    This is only a test.\t\t")
    assert result == "This is a test. This is only a test."
    
#2.for null chars

def test_null_char():
    res = clean_text("This is a test.\x00This is only a test.")
    assert res == "This is a test.This is only a test."
#3. normalize line ending
def test_normalize_line_endings():
    res = clean_text("hello\r\nworld")  
    assert res == "hello\nworld" 
#4. exsessive blank line 

def test_remove_excessive_blank_lines():
    result = clean_text("Hello\n\n\n\nWorld")
    assert result == "Hello\n\nWorld"
#5. empty text
def test_empty():
    assert clean_text("") == ""   
#6. whitespace
def test_white_space():
    assert clean_text("   \n   ") == ""         

     
        