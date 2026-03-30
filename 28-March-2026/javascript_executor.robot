*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${url}  https://inc.in/

*** Test Cases ***
handling js
    Open Browser    ${url}  chrome
    Maximize Browser Window
    Sleep    2s


    Execute Javascript  window.scrollTo(0,document.body.scrollHeight)
    Sleep    3s
    Execute Javascript  window.scrollBy(1000,0)
    Sleep  2s
    Close Browser