*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${url}  https://demo.automationtesting.in/Frames.html

*** Test Cases ***
Handling Single IFrame
    Open Browser    ${url}  chrome
    Maximize Browser Window
    Sleep    2s

    Select Frame    id=singleframe

    Input Text    xpath=//input[@type="text"]    Peoples
    Sleep    2s
    Unselect Frame
    
    Click Element    xpath=(//a[@class="analystic"])[2]

    Select Frame    xpath=//iframe[@src="MultipleFrames.html"]
    Select Frame    xpath=//iframe[@src="SingleFrame.html"]
    Sleep    3s
    Input Text    xpath=//input[@type="text"]    Hello
    Sleep    3s
    Unselect Frame
    Unselect Frame


    Click Element    xpath=(//a[@class="analystic"])[1]
    Sleep    3s
    Close Browser