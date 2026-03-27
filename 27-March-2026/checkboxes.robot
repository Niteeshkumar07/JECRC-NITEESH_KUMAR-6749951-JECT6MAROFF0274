*** Settings ***
Documentation  handling checkboxes
Library  SeleniumLibrary

*** Variables ***
${url}  https://the-internet.herokuapp.com/
${url1}  https://testautomationpractice.blogspot.com/
*** Test Cases ***
Handling Checkboxes
    [Documentation]  herokuapp checkboxes
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep  1s

    Click Element    xpath=//a[text()="Checkboxes"]
    Page Should Contain Checkbox    xpath=//input[@type="checkbox"]
    Select Checkbox    xpath=(//input[@type="checkbox"])[1]
    Sleep    3s
    Unselect Checkbox    xpath=(//input[@type="checkbox"])[2]
    Sleep    3s
    Close Browser

Handling few Checkboxes
    [Documentation]  handling few checkboxes
    Open Browser  ${url1}  chrome
    Maximize Browser Window
    Sleep    3s

    Select Checkbox    id=sunday
    Select Checkbox    id=monday
    Sleep    3s
    Close Browser
