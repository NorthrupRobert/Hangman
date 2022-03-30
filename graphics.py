def TitleScreen():
	print(""".-. .-.  .--.  .-. .-. .---. .-.   .-.  .--.  .-. .-.
| {_} | / {} \ |  `| |/   __}|  `.'  | / {} \ |  `| |
| { } |/  /\  \| |\  |\  {_ }| |\ /| |/  /\  \| |\  |
`-' `-'`-'  `-'`-' `-' `---' `-' ` `-'`-'  `-'`-' `-'""")

def Lose():
	print("""      ██████▒▒▒▒░░░░    ░░░░░░░░        ▒▒██▓▓▓▓▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▓▓██████▓▓▓▓░░                
    ░░██████▒▒░░░░    ░░░░░░        ░░▒▒████▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▓▓██████▓▓▓▓░░                
    ▓▓████▒▒░░░░░░░░▒▒░░░░      ░░▒▒██████▒▒░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒░░░░▒▒▓▓██████▓▓▓▓▒▒                
    ▓▓████░░░░░░░░░░▒▒░░        ██████▓▓▒▒░░░░░░        ░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒▓▓██████▓▓▓▓                
    ▓▓██▓▓▒▒░░░░░░▒▒░░░░        ██▒▒░░░░░░  ░░      ░░░░░░░░▓▓▒▒▒▒▒▒░░░░░░░░░░▒▒░░▓▓██▓▓▓▓▓▓▓▓                
    ▓▓██▒▒▒▒░░  ▒▒▒▒░░        ▒▒▒▒░░░░        ░░░░░░░░░░░░░░▒▒▒▒░░░░░░░░░░░░░░░░░░▒▒████▓▓▓▓▓▓░░              
  ▒▒▓▓▓▓▒▒░░░░░░▒▒░░░░      ░░▒▒░░          ░░▓▓▓▓▒▒░░░░░░░░▒▒▓▓▓▓▒▒░░░░░░░░░░▒▒░░░░████████▓▓▓▓              
  ▓▓▓▓▒▒▒▒░░░░░░▒▒░░░░    ░░▓▓░░        ░░▒▒██▓▓▓▓░░░░░░░░▒▒▓▓▒▒░░░░░░░░░░░░░░░░░░░░▓▓██████▓▓▓▓              
  ████░░░░░░░░░░▒▒░░░░    ░░░░░░        ░░▓▓▓▓▓▓▓▓▒▒░░░░░░░░▒▒░░▒▒▒▒▒▒░░░░░░░░░░░░░░▒▒██████▓▓██▓▓            
░░████░░░░░░░░░░░░░░░░  ░░▒▒░░░░      ░░▓▓▓▓██▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░  ░░░░░░▓▓▓▓██████▓▓░░          
░░████░░░░░░░░▒▒░░░░░░░░░░░░░░░░    ░░▒▒▒▒▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░    ░░░░░░▓▓██▓▓██▓▓▓▓▓▓▓▓        
  ▓▓██░░░░░░░░░░░░░░░░░░░░░░░░      ░░░░▒▒▓▓▓▓▓▓▒▒░░░░░░░░░░░░░░▒▒░░░░░░          ░░░░░░▓▓▓▓██▓▓▓▓▓▓▓▓░░      
  ▓▓██░░░░░░▒▒░░░░░░░░░░░░░░        ░░░░▒▒▒▒▓▓▓▓░░░░░░░░  ░░░░░░░░▒▒▒▒░░            ░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░      
  ▓▓██▒▒░░░░▒▒░░░░░░░░░░░░          ░░░░░░▒▒▓▓▒▒░░░░░░░░░░░░░░░░░░░░▒▒░░            ░░░░▓▓▓▓▓▓▓▓▓▓▓▓▒▒        
  ▓▓██▒▒░░░░▒▒░░░░░░░░░░░░          ░░░░░░▓▓▓▓▓▓▒▒▒▒░░░░░░██▓▓░░░░░░░░▒▒░░          ░░░░▓▓██▓▓▒▒▒▒▒▒░░        
  ▓▓██▒▒░░░░░░░░░░░░░░░░░░          ░░░░░░▓▓▓▓▒▒████▓▓░░░░▒▒░░░░░░░░░░░░▒▒░░      ░░░░░░▓▓██▓▓▓▓▒▒▒▒▒▒        
  ████▒▒▒▒▒▒░░░░░░░░░░░░░░            ░░▒▒▓▓▓▓▓▓▓▓▓▓▒▒▒▒░░░░░░░░░░░░░░░░░░▒▒░░░░  ░░░░░░▒▒▒▒▒▒░░▒▒▒▒░░        
  ████░░▒▒▒▒░░░░░░░░░░░░░░            ░░▒▒▒▒▓▓▓▓▓▓▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░▒▒░░░░░░░░░░░░▒▒▒▒░░▒▒░░          
░░██▓▓▒▒▒▒▒▒░░░░░░░░░░░░░░            ░░▒▒▒▒▒▒▓▓▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░            
░░██▓▓▒▒▒▒▒▒░░░░░░░░░░░░░░            ░░▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒░░░░░░░░░░░░░░░░              
░░▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░              ▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒░░░░░░░░░░  ░░░░              
  ▒▒▓▓██░░▒▒░░░░░░░░░░░░░░              ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░▒▒▓▓▒▒░░░░░░░░░░░░░░  ░░░░░░              
  ░░████░░▒▒░░░░░░░░░░░░░░              ▒▒▒▒▓▓▓▓▒▒▓▓▒▒▒▒▒▒░░░░      ░░░░▓▓▒▒░░▒▒░░░░░░░░▓▓▓▓▒▒░░              
      ▓▓░░▒▒░░░░░░░░░░░░                ▒▒▒▒▓▓▓▓▒▒░░░░                  ░░▓▓▒▒▒▒░░░░░░░░██▓▓▓▓▒▒              
      ▓▓▒▒▒▒░░░░░░░░░░                  ▒▒▒▒▓▓▓▓░░░░░░                  ░░▓▓▒▒░░░░░░░░░░████▒▒▒▒              
        ▒▒░░░░░░░░░░░░                  ▒▒▒▒▓▓▒▒▒▒░░        ░░████▓▓▒▒▒▒▓▓▒▒▒▒░░░░░░░░░░░░▒▒▒▒                
        ░░░░░░░░░░░░░░                  ▒▒▒▒▓▓▒▒▒▒░░░░▓▓▓▓████████████▓▓▓▓▒▒░░░░░░░░░░░░▓▓▓▓░░                
          ▒▒░░░░░░░░░░                  ▒▒▓▓▒▒▒▒░░▓▓▓▓██████████████████▓▓▒▒░░░░▒▒░░░░░░██▓▓░░░░              
        ░░░░░░░░░░░░░░                ░░░░▒▒▓▓▓▓▓▓▓▓██████████▓▓░░░░▒▒████▒▒░░░░▒▒░░░░░░██▓▓▓▓░░              
          ▒▒░░░░░░░░░░                ░░▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓██▓▓▒▒░░░░░░░░░░▒▒▒▒░░░░░░░░░░░░██▓▓▓▓▒▒              
          ▒▒░░░░░░░░                  ░░▒▒▒▒▒▒▓▓▓▓▓▓▒▒░░░░▒▒░░░░░░      ▒▒░░░░░░░░░░░░░░██▓▓░░                
        ░░░░░░░░                    ░░░░▒▒▒▒▒▒▒▒▓▓▒▒░░░░░░            ░░▒▒░░░░░░░░░░░░░░▒▒░░░░                
        ░░░░░░░░                ░░░░░░▓▓░░▒▒▒▒▒▒▒▒░░░░░░      ░░  ░░░░░░░░░░░░░░░░░░░░░░░░                    
        ░░░░░░                ░░░░░░▒▒▓▓░░▓▓▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░                      
      ░░░░░░                  ░░░░▒▒▒▒▒▒▒▒░░▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░                      
      ░░░░░░                ░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░                      
    ░░░░░░░░░░              ░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░                      
  ░░░░░░░░░░░░░░          ░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░                    
░░░░░░░░░░░░░░          ░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░                    
░░░░░░░░░░░░░░          ░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░                    
░░░░░░░░░░░░░░        ░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  ░░░░  ░░      
░░░░░░░░░░░░░░      ░░░░░░      ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░▒▒░░░░░░░░░░░░░░░░░░░░░░░░  ░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░      ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒░░▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░  ░░░░░░    ░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░        ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░        ░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░        ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░          ░░░░░░
░░░░░░░░░░░░░░░░░░░░░░      ░░▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░          ░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒██▓▓▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░      ░░░░░░""")

def Win():
	print("""                                                                      
                    ▓▓▓▓    ▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓                        
                    ▓▓░░▓▓▓▓░░░░▒▒░░░░░░░░░░░░▓▓▓▓▓▓                  
                ▒▒▒▒▓▓▒▒▒▒▒▒░░░░▒▒░░░░░░░░░░░░░░▒▒▓▓▒▒▒▒              
                ▓▓▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▓▓              
                  ▓▓▒▒▓▓░░░░░░▒▒░░░░▒▒▒▒░░░░░░▓▓░░░░▓▓                
                ▓▓░░▒▒░░▓▓▓▓░░░░▓▓▓▓░░░░▓▓▓▓░░░░▓▓░░░░▓▓              
                ▓▓░░░░▓▓░░░░▒▒▒▒░░░░▓▓▒▒░░░░▓▓▒▒░░▒▒░░▓▓              
                ▓▓░░▒▒▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▓▓              
                ▒▒░░░░▓▓░░░░░░░░▓▓▓▓▒▒░░░░░░▓▓▓▓▓▓░░▒▒                
                ▒▒▒▒░░▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒              
      ▒▒▒▒▒▒▒▒▒▒░░░░▓▓▓▓░░░░░░░░████░░░░░░░░░░████░░▒▒░░▒▒▒▒▒▒▒▒▓▓    
    ▒▒░░░░░░░░▒▒░░░░▓▓░░░░░░░░░░████░░░░░░░░░░████░░▒▒░░▒▒░░░░░░░░▒▒  
    ▒▒░░░░░░░░▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒░░░░░░░░▒▒  
    ▒▒░░░░░░░░▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒░░░░░░░░▒▒  
    ▒▒░░▒▒▒▒▒▒    ▒▒▒▒░░░░░░░░▒▒░░░░░░░░░░░░░░░░░░░░▒▒    ▒▒▒▒▒▒░░▒▒  
    ▒▒░░░░░░▒▒    ▒▒░░░░░░░░░░░░▒▒▒▒▒▒▒▒░░░░░░░░░░░░▒▒    ▒▒░░░░░░▒▒  
    ▒▒░░░░░░▒▒    ▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒    ▒▒░░░░░░▒▒  
    ▒▒░░░░░░▒▒    ░░▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒░░    ▒▒░░░░░░▒▒  
    ░░▒▒░░░░░░▒▒    ▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒    ▒▒░░░░░░▒▒░░  
      ▓▓▒▒░░░░▓▓      ▒▒░░░░░░░░░░░░░░░░░░░░░░░░▓▓      ▓▓░░░░▒▒▓▓    
      ▓▓▒▒░░░░░░▓▓      ▒▒▒▒░░░░░░░░░░░░░░░░▒▒▒▒      ▓▓░░░░░░▒▒▓▓    
        ▓▓▒▒░░░░░░▓▓▓▓      ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒      ▓▓▓▓░░░░░░▒▒▓▓      
        ▓▓▒▒░░░░░░░░░░▓▓▓▓▓▓▓▓      ▓▓▒▒    ▓▓▓▓▓▓░░░░░░░░░░▒▒▓▓      
          ▓▓▒▒░░░░░░░░░░░░░░▓▓    ▓▓▒▒▓▓▓▓  ▓▓░░░░░░░░░░░░▒▒▓▓        
            ▓▓▒▒▒▒░░░░░░░░░░░░▓▓  ▓▓▒▒▓▓▓▓  ▓▓░░░░░░░░▒▒▒▒▒▒          
              ▓▓▓▓▒▒░░░░░░░░░░░░▓▓  ░░░░░░▓▓░░░░░░░░▒▒▓▓▓▓            
                  ▓▓▒▒░░░░░░░░░░▓▓  ▒▒▒▒  ▓▓░░░░░░▒▒▓▓                
                    ▓▓▒▒▒▒░░░░░░▓▓  ▒▒▒▒  ▓▓░░░░░░▓▓                  
                      ▓▓▒▒▒▒░░░░░░▓▓▒▒▒▒▓▓░░░░░░▓▓                    
                      ▓▓▒▒▒▒░░░░░░▒▒▒▒▒▒▓▓░░░░░░▓▓                    
                      ▓▓▒▒▒▒░░░░░░▓▓▒▒▓▓▓▓░░░░░░▓▓                    
                      ▓▓▒▒▒▒░░░░░░░░▓▓▓▓░░░░░░░░▓▓                    
                      ▓▓▒▒▒▒░░░░░░░░▒▒▒▒░░░░░░░░▓▓                    
                      ▓▓▒▒▒▒░░░░░░▓▓▒▒▒▒░░░░░░░░▓▓                    
                      ▓▓▒▒▒▒░░░░░░░░▒▒▓▓░░░░░░░░▓▓                    
                      ▓▓▒▒▒▒░░░░░░░░▒▒▓▓░░░░░░░░▓▓                    
                      ▓▓▒▒▒▒░░░░░░░░▒▒▓▓░░░░░░░░▓▓                    
                      ▓▓▒▒▒▒░░░░░░▓▓▒▒▓▓░░░░░░░░▓▓                    
                      ▓▓▒▒▒▒░░░░░░░░▒▒▒▒░░░░░░░░▓▓                    
                      ▓▓▒▒▒▒░░░░░░░░▒▒▒▒░░░░░░░░▓▓                    
                      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                    
                      ▓▓▒▒▒▒░░░░░░▓▓▓▓▒▒▒▒▒▒░░░░▓▓                    
                      ▓▓▒▒▒▒░░░░▓▓  ░░▓▓▒▒▒▒░░░░▓▓                    
                      ▓▓▒▒▒▒░░░░▓▓  ░░▓▓▒▒▒▒░░░░▓▓                    
                      ▓▓▒▒▒▒░░░░▓▓  ░░▓▓▒▒▒▒░░░░▓▓                    
                      ▓▓▒▒▒▒░░░░▓▓  ░░▓▓▒▒▒▒░░░░▓▓                    
                      ▓▓▒▒▒▒░░░░▓▓  ░░▓▓▒▒▒▒░░░░▓▓                    
                      ▓▓▒▒▒▒░░░░▓▓  ░░▓▓▒▒▒▒░░░░▓▓                    
                      ▓▓▒▒▒▒░░░░▓▓  ░░▓▓▒▒▒▒░░░░▓▓                    
                      ▓▓▒▒▒▒░░░░▓▓  ░░▓▓▒▒▒▒░░░░▓▓                    
                      ▓▓▒▒▒▒░░░░▓▓  ░░▓▓▒▒▒▒░░░░▓▓                    
                      ▓▓▒▒▓▓▓▓▓▓▓▓  ░░▓▓▒▒▓▓▓▓▓▓▓▓                    
                      ▓▓▓▓▒▒▒▒░░░░▓▓░░▓▓▓▓▒▒▒▒░░░░▓▓                  
                      ▓▓▒▒▒▒▒▒▒▒░░▓▓░░▓▓▒▒▒▒▒▒▒▒░░▓▓                  
                      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓                  
                                                                      
                                                                      
    ▓▓▓▓▓▓  ▓▓    ▓▓    ▓▓▓▓▓▓    ▓▓▓▓▒▒    ▓▓▓▓      ▓▓▓▓▓▓    ▓▓▓▓▓▓
░░▓▓        ▓▓    ▓▓  ▓▓        ▓▓        ▓▓    ▓▓  ▓▓        ▓▓      
  ░░▓▓▓▓    ▓▓    ▓▓  ▓▓        ▓▓        ▓▓▓▓▓▓▓▓    ▓▓▓▓      ▓▓▓▓  
        ▓▓  ▓▓    ▓▓  ▓▓        ▓▓        ▓▓              ▓▓        ▓▓
░░▓▓▓▓██      ▓▓▓▓▓▓    ▓▓▓▓██    ▓▓▓▓▒▒    ▓▓▓▓▓▓  ▓▓▓▓▓▓    ▓▓▓▓▓▓  
""")