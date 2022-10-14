import pywinauto
from pywinauto import application
from pywinauto.application import Application
import time
import pywinauto.mouse as mouse
import pywinauto.keyboard as keyboard


def CipSimulator_Start():    
    #Launching CIP Simulator and press "Start" Button
    app = Application().Start(cmd_line=u'"C:\\Alstom\\simuERTMSforTWINS\\simuERTMSforTWINS.exe" ')
    time.sleep(2)
    window = app.Dialog
    window.Wait('ready')
    button = window.Button
    button.Click()
    time.sleep(2)


    #Closing "STM Header" window
    stm_window = app.Dialog
    stm_window.Wait('ready')
    #Double click the STM id field
    edit = stm_window.Edit
    edit.ClickInput()

    stm_window[u'STM_NID_STMEdit'].type_keys("2")
    time.sleep(1)

    stm_window.Close()
    time.sleep(2)

def CipSimulator_EVCtoDMI_TelegramMode():
    #Selecting "Communication", "Message to Send", writing telegram, sending the telegram
    app = Application().connect(path=r"C:\Alstom\simuERTMSforTWINS\simuERTMSforTWINS.exe")
    window = app.Dialog
    window.wait('ready')
    combobox = window.ComboBox
    combobox.select(u'EVC-->DMI1')

    time.sleep(2)

    #Selecting 'Message to send'
    combobox = window.ComboBox2
    combobox.select(u'User defined hexadecimal telegram')

    time.sleep(1)

def CipSimulator_STM1toDMI_TelegramMode():
    #Selecting "Communication", "Message to Send", writing telegram, sending the telegram
    app = Application().connect(path=r"C:\Alstom\simuERTMSforTWINS\simuERTMSforTWINS.exe")
    window = app.Dialog
    window.wait('ready')
    combobox = window.ComboBox
    combobox.select(u'STM1<-->DMI1')
    time.sleep(2)

    #Closing "STM Header" window
    stm_window = app.Dialog
    stm_window.Wait('ready')
    #Double click the STM id field
    edit = stm_window.Edit
    edit.ClickInput()

    stm_window[u'STM_NID_STMEdit'].type_keys("8")
    time.sleep(1)

    #Selecting 'Message to send'
    combobox = window.ComboBox2
    combobox.select(u'User defined hexadecimal telegram')

    time.sleep(1)

def CipSimulator_SendTelegramToDMI(Telegram):
    #Writting telegram in the "Telegram Contents" edit field
    app = Application().connect(path=r"C:\Alstom\simuERTMSforTWINS\simuERTMSforTWINS.exe")
    window = app.Dialog
    window.wait('ready')
    edit = window.Edit
    edit.click_input()

    #Telegram_To_Send = str("AA BB CC DD")
    window[u'Telegram contents (hexadecimal)Edit'].set_edit_text(u'') #Clean up the existing contents
    window[u'Telegram contents (hexadecimal)Edit'].type_keys(str(Telegram))

    time.sleep(10)
    #Sending the telegram
    window = app.Dialog
    window.Wait('ready')
    window[u'Send 1 packetButton'].click()
    time.sleep(1)
    window[u'Send 1 packetButton'].click()

def CipSimulator_Close():
    app = Application().connect(path=r"C:\Alstom\simuERTMSforTWINS\simuERTMSforTWINS.exe")
    app.Kill_()

def Get_Delay(value):
    time.sleep(int(value))


#button = window.Button2
#button.Click()

#Closing the application
#app.Kill_()




