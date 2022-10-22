from botcity.core import DesktopBot

class Bot(DesktopBot):
    def action(self, execution=None):
        self.browse("https://www.instagram.com/")
        count = 0
        
        while count <= 5:       
          
          if not self.find( "acessando_storie", matching=0.97, waiting_time=20000):
            self.not_found("acessando_storie")
          self.click()
          
          if not self.find( "curtindo", matching=0.97, waiting_time=20000):
            self.not_found("curtindo")
          self.click()         
          
          if not self.find( "saindo", matching=0.97, waiting_time=20000):
            self.not_found("saindo")
          self.click()
          count += 1

          def key_f5(self, wait=0):
                self._key_fx(5, wait=wait)
          
          key_f5
          



if __name__ == '__main__':
    Bot.main()