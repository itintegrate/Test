#This is API can create Chart and image using 'pip3 install matplotlib'
import matplotlib.pyplot as plt  
#This is API can get elements from HTML using 'pip3 install beautifulsoup4' 
import bs4 as bs 
#This is API can get HTML data by request url using 'pip install urllib3'                
import urllib.request 
#This is solve ssl block issues already in python3 pagckage
import ssl

#This is solve ssl block issues
ssl._create_default_https_context = ssl._create_unverified_context

class GetChart():

    def __init__(self):        
        self.data =[]
        self.td_index = 0
        self.final_index = 0

    #Console input URL function return url address
    def url_input(self):
        url_var = input("Please enter URL: ")
        t_url = str(url_var).replace(' ','')
        return t_url           

    #Connect to URL get HTML data back
    def conn_req(self):
        try:

            #Send request
            sauce_t = urllib.request.urlopen(self.url_input(),timeout=50).read().decode('utf-8')
        except:

            #If error will return string
            print('Error, Something wrong on this url')
            return "something error"  
        else:           
            print('main Access successful.')

        #Using bs4 to convert HTML data to getable data    
        soup_t = bs.BeautifulSoup(sauce_t,'html.parser')
        return soup_t

    #Main processing to get table data and find numeric data
    def processing(self):

        #Get HTML Data
        soup_t = self.conn_req()

        #if connection is error or un connected 
        if soup_t == "something error":
            print("Please try it again")
            return
        try:

            # 1 try to numeric data from sortable table
            self.get_data(soup_t,"sortable")

        except:
            try:

                # 2 try to numeric data from other wiki table
                self.get_data(soup_t,"wikitable")

            except:

                # 3 if no table print "can not find any tables"
                print("can not find any tables...")
                return

        #Checking data have any Numeric data array
        if not self.data:
            print("Not Numeric data in this table")
            return

        #Genertor Chart and Image
        self.gen_chart()

    # fc: Get data from different tables 
    def get_data(self, soup_t, table_type):

        # Using bs4 to find table by table types like sortable table or wiki table
        t_table = soup_t.find('table',{'class':table_type})
       
        # This will find index of numeric column saved into self.final_index 
        self.working_on_table(t_table)       

        # Get Length of tr of table
        total_length = len(t_table.find_all('tr'))    

        # Get and Checking numeric number and save into self.data
        for eachItem in range(total_length):
            try:
                # Get table numeric number by td index from tr
                temp_value = t_table.find_all('tr')[eachItem].find_all('td')[self.final_index].text

                # Split the string to find first numeric number or it just numeric number
                for num in temp_value.split():
                    if num.isnumeric():
                        # Save numeric number
                        self.data.append(num)
                        break     
            except:
                continue 

        
    # fc: Get number column index
    def working_on_table(self,t_table):

        value_len = len(t_table.find_all('tr')[self.td_index].find_all('td'))
        # Try to find first td cell
        if value_len == 0:            
            self.td_index+=1
            self.working_on_table(t_table)
        else:
            #Get all the td element
            value = t_table.find_all('tr')[self.td_index].find_all('td')

            # Find first numeric number index of these tds
            final_index = self.checking_num_loop(value_len,value) 

            # Save the numeric number td index           
            self.final_index = final_index
    
    #fc: get each td values and find numeric value return numeric column index
    def checking_num_loop(self,lens,item):  
        for each in range(lens):
            item_value = item[each].text
            # return td index, else return first td index     
            if self.get_num_item(item_value):                
                return each
        return 0
                
    #fc: finding first numeric value from tds return True
    def get_num_item(self,item_value):
        #if value is numeric will return
        if item_value.isnumeric():            
            return True

        #eles split string to find element has numeric value
        for num in item_value.split():
            if num.isnumeric():                
                return True

    #fc export Chart image
    def gen_chart(self):
        #plot numbers
        plt.plot(self.data) 
        #save to png
        plt.savefig('plot.png', dpi=500, bbox_inches='tight')



if __name__ =='__main__':
    #new object 
    getChart = GetChart()
    #run the function
    getChart.processing()
    print("image called 'plot.png' it is inside same folder of is program")


