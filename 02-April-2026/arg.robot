*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${url}  https://sauce-demo.myshopify.com/account/login

*** Test Cases ***
Login
    Open Browser    ${url}  chrome
    Sleep    3s
    Login Success    cheeseburger@gmail.com     123455  #Positional
#    Login Success    email=we@gmail.com    pwd=123456789098765432  Keyword
    Sleep    3s

    Close Browser

*** Keywords ***
Login Success
    [Arguments]     ${email}    ${password}
    Input Text    id=customer_email    ${email}
    Input Text    id=customer_password    ${password}


