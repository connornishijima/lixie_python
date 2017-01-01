import os
import time

logo = ""
logo += "888      8888888 Y88b   d88P 8888888 8888888888\n"
logo += "888        888    Y88b d88P    888   888       \n"
logo += "888        888     Y88o88P     888   888       \n"
logo += "888        888      Y888P      888   8888888   \n"
logo += "888        888      d888b      888   888       \n"
logo += "888        888     d88888b     888   888       \n"
logo += "888        888    d88P Y88b    888   888       \n"
logo += "88888888 8888888 d88P   Y88b 8888888 8888888888\n"

logo_width = 47
logo_height = 10

def center_screen(text,width,height):
        text = text.split("\n")
        rows, columns = os.popen('stty size', 'r').read().split()
        os.system("clear")
        top = (int(rows)/2)-(int(height)/2)
        for i in range(top):
                print ""
        left = (int(columns)/2)-(int(width)/2)
        for item in text:
                print (" "*left)+item

def center_line(text):
        rows, columns = os.popen('stty size', 'r').read().split()
        left = (int(columns)/2)-(int(len(text))/2)
        print (" "*left)+text

def update():
        title("Updating repositories...")
        os.system("sudo apt-get update")
        title("Upgrading Raspberry Pi...")
        os.system("sudo apt-get upgrade")

def title(text):
        print "\n"
        rows, columns = os.popen('stty size', 'r').read().split()
        print "-"*int(columns)
        center_line(text)
        print "-"*int(columns)
        print "\n"

def install():
        title("Cloning rpi_ws281x...")
        os.system("sudo git clone https://github.com/jgarff/rpi_ws281x.git")
        os.chdir("rpi_ws281x")
        title("Installing scons...")
        os.system("sudo apt-get install scons")
        title("Compiling rpi_ws281x...")
        os.system("sudo scons")

        title("Checking for I2S audio blacklisting...")
        with open("/etc/modprobe.d/snd-blacklist.conf","a+") as f:
                data = f.read()

        if not "snd_bcm2835" in data:
                center_line("Blacklisting the Broadcom I2S audio kernel module...")
                with open("/etc/modprobe.d/snd-blacklist.conf","a+") as f:
                        f.write("blacklist snd_bcm2835\n")
        else:
                center_line("I2S audio already blacklisted.")

        os.chdir("..")
        title("Removing rpi_ws281x clone directory...")
        os.system("sudo rm -r rpi_ws281x")
        center_line("Done.")
        title("Cloning lixie_python...")
        os.system("sudo git clone https://github.com/connornishijima/lixie_python.git")
        os.chdir("lixie_python")
        center_line("Done.")
        title("Installing Lixie to /usr/lib/python2.7...")
        os.system("sudo cp lixie.py /usr/lib/python2.7")
        os.chdir("..")
        center_line("Done.")
        title("Removing lixie_python clone directory...")
        os.system("sudo rm -r lixie_python")
        center_line("Done.")

def lixie_demo():
        import lixie as lix
        lix.begin(6)
        count = 0
        while True:
                lix.write(count)
                time.sleep(0.1)
                count+=1

def intro():
        center_screen(logo,logo_width,logo_height)
        center_line("----------- PYTHON LIBRARY INSTALLER ----------")
        print "\n"
        center_line("This script will take care of installing")
        center_line("Lixie and all of its dependencies.")
        print ""
        center_line("Ready to go? (y/n)")

        answer = raw_input()
        if answer.lower() == "y" or answer.lower() == "yes":
                update()
                install()
                finish()
        else:
                center_screen("Install cancelled.",18,1)
                center_line("We could have had something beautiful.")

def finish():
        os.system("clear")
        text = "Lixie Python Library install finished! Thanks!"
        center_screen(text,len(text),1)
        print ""
        center_line("If you already have Lixies wired correctly, you should see a counting animation!")
        center_line("Press Crtl+C to finish...")
        print "\n\n\n"
        lixie_demo()

intro()
