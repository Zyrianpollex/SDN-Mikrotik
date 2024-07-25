import tkinter as tk
import requests
import json


# Define the API endpoint
ip =""
#ip = "test"
url = ""
#url = "https://admin:123@192.168.22.1/rest/"

class MyApp(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("My App")
        self.geometry("800x600")
        
        self.frames = {}
        
        # create and add the frames to a dictionary
        for F in (StartPage, 
        PageInterfaces, 
        PageWireless,
        PageBridges,PageBridges_intefaces,PageBridges_intefaces_Criar,PageBridges_intefaces_Editar,PageBridges_intefaces_Delete,
        PageBridges_Port_inteface_List,PageBridges_Port_inteface_Create,PageBridges_Port_inteface_Patch,PageBridges_Port_inteface_Delete,
        PageSecurityProfiles,PageSecurityProfiles_Put,PageSecurityProfiles_Patch,PageSecurityProfiles_Delete,
        PageWireless_Redes,PageWireless_Redes_Ativar,PageWireless_Redes_Desativar,PageWireless_Redes_Configurar,
        PageStatic_routes,PageStatic_routes_Listar,PageStatic_routes_Criar,PageStatic_routes_Editar,PageStatic_routes_Apagar,
        PageIp_Address,PageIp_Address_Listar,PageIp_Address_Criar,PageIp_Address_Editar,PageIp_Address_Apagar,
        PageDHCP,PageDHCP_Listar,PageDHCP_Criar,PageDHCP_Editar,PageDHCP_Apagar,
        PageWirewall,PageWirewall_Listar,PageWirewall_Criar,PageWirewall_Editar,PageWirewall_Apagar,
        PageDNS,PageDNS_Ativar,PageDNS_Desativar,PageDNS_Configurar,
        PageProtocoloEncaminhamento,PageProtocoloEncaminhamento_Criar_Instancia,PageProtocoloEncaminhamento_Criar_Area, PageProtocoloEncaminhamento_Criar_Interface_Template,PageProtocoloEncaminhamento_Ativar,PageProtocoloEncaminhamento_Desativar,
        PageVPN):
            frame = F(self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        
        self.show_frame(StartPage)
        
    def show_frame(self, page):
        """Show a frame for the given page"""
        frame = self.frames[page]
        frame.tkraise()
        
class StartPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        
        #entry = tk.Entry(self, textvariable=self.entry_text)
        #entry.pack(pady=5, padx=10)
        label = tk.Label(self, text="This is the start page")
        label.pack(pady=10, padx=10)

        label = tk.Label(self, text="IP")
        label.pack(pady=10, padx=10)

        global ip_Text
        ip_Text = tk.Text(self,height = 1, width = 20)
        ip_Text.pack()

        label = tk.Label(self, text="User")
        label.pack(pady=10, padx=10)

        global user_Text
        user_Text = tk.Text(self,height = 1, width = 20)
        user_Text.pack()
        
        label = tk.Label(self, text="Password")
        label.pack(pady=10, padx=10)

        global password_Text
        password_Text = tk.Text(self,height = 1, width = 20)
        password_Text.pack()

        
        button_Submit = tk.Button(self, text="Submit", command=submit_text)
        button_Submit.pack(pady=5, padx=10)

        global StartPage_display_text
        StartPage_display_text = tk.Label(self, text="")
        StartPage_display_text.pack(pady=10, padx=10)

        
        
        button_interfaces = tk.Button(self, text="Go to Page interfaces", command=lambda: master.show_frame(PageInterfaces))
        button_interfaces.pack()

        button_Wireless = tk.Button(self, text="Go to Page Wireless", command=lambda: master.show_frame(PageWireless))
        button_Wireless.pack()

        button_bridge = tk.Button(self, text="Go to Page bridge", command=lambda: master.show_frame(PageBridges))
        button_bridge.pack()

        button_bridge = tk.Button(self, text="Go to security-profiles Page", command=lambda: master.show_frame(PageSecurityProfiles))
        button_bridge.pack()

        button_bridge = tk.Button(self, text="Go to Wireless_Redes Page", command=lambda: master.show_frame(PageWireless_Redes))
        button_bridge.pack()

        button_bridge = tk.Button(self, text="Go to ip address Page", command=lambda: master.show_frame(PageIp_Address))
        button_bridge.pack()

        button_bridge = tk.Button(self, text="Go to DHCP Page", command=lambda: master.show_frame(PageDHCP))
        button_bridge.pack()

        button_bridge = tk.Button(self, text="Go to Firewall Page", command=lambda: master.show_frame(PageWirewall))
        button_bridge.pack()

        button_bridge = tk.Button(self, text="Go to DNS Page", command=lambda: master.show_frame(PageDNS))
        button_bridge.pack()

        button_bridge = tk.Button(self, text="Go to Protocolos de encaminhamento", command=lambda: master.show_frame(PageProtocoloEncaminhamento))
        button_bridge.pack()

        button_bridge = tk.Button(self, text="Go to VPN", command=lambda: master.show_frame(PageVPN))
        button_bridge.pack()


 #pagina da interfaces       
class PageInterfaces(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        
        label = tk.Label(self, text="interfaces page")
        label.pack(pady=10, padx=10)

        #url = url + 'interface'
        button = tk.Button(self, text='Listar todas as interfaces', command=listar_intefaces)
        button.pack()

        global response_label
        response_label = tk.Text(self)
        response_label.pack()
        
        
        button1 = tk.Button(self, text="Go to Start Page", command=lambda: [delete_text(),master.show_frame(StartPage)])
        button1.pack()  


        
class PageWireless(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        
        label = tk.Label(self, text="This is page Wireless")
        label.pack(pady=10, padx=10)

        button_listar_wireless = tk.Button(self, text='Listar todas as interfaces Wireless', command=listar_intefaces_wireless)
        button_listar_wireless.pack()

        global response_label_wireless
        response_label_wireless = tk.Text(self)
        response_label_wireless.pack()

        
        button = tk.Button(self, text="Go to Start Page", command=lambda:[delete_text_wireless(),master.show_frame(StartPage)])
        button.pack()


class PageBridges(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        

        button = tk.Button(self, text="List brige interfaces", command=lambda:[delete_text_wireless(),master.show_frame(PageBridges_intefaces)])
        button.pack()

        button = tk.Button(self, text="Criar brige interfaces", command=lambda:[delete_text_wireless(),master.show_frame(PageBridges_intefaces_Criar)])
        button.pack()
        
        button = tk.Button(self, text="Go to Edit brige interface", command=lambda:master.show_frame(PageBridges_intefaces_Editar))
        button.pack()

        button = tk.Button(self, text="Go to Delete brige interface", command=lambda:master.show_frame(PageBridges_intefaces_Delete))
        button.pack()

        button = tk.Button(self, text="Go to List brige Ports", command=lambda:master.show_frame(PageBridges_Port_inteface_List))
        button.pack()

        button = tk.Button(self, text="Go to Create brige Ports Interface", command=lambda:master.show_frame(PageBridges_Port_inteface_Create))
        button.pack()

        button = tk.Button(self, text="Go to PATCH brige Ports Interface", command=lambda:master.show_frame(PageBridges_Port_inteface_Patch))
        button.pack()

        button = tk.Button(self, text="Go to DELETE brige Ports Interface", command=lambda:master.show_frame(PageBridges_Port_inteface_Delete))
        button.pack()

        button = tk.Button(self, text="Go to Start Page", command=lambda:[delete_text_wireless(),master.show_frame(StartPage)])
        button.pack()


class PageBridges_intefaces(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        
        label = tk.Label(self, text="This is page Wireless")
        label.pack(pady=10, padx=10)

        button_listar_Bridges = tk.Button(self, text='Listar todas as interfaces Bridge', command=listar_intefaces_Bridge)
        button_listar_Bridges.pack()

        global response_label_bridges
        response_label_bridges = tk.Text(self)
        response_label_bridges.pack()

        
        button = tk.Button(self, text="Go Back", command=lambda:[delete_text_brige(),master.show_frame(PageBridges)])
        button.pack()

class PageBridges_intefaces_Criar(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        
        label = tk.Label(self, text="Name of the Brige:")
        label.pack(pady=10, padx=10)

        global Brige_Name_Text
        Brige_Name_Text = tk.Text(self,height = 1, width = 20)
        Brige_Name_Text.pack()

        
        button_Submit_Brige = tk.Button(self, text="Submit", command=submit_Brige)
        button_Submit_Brige.pack(pady=5, padx=10)

        #global StartPage_display_text
        #StartPage_display_text = tk.Label(self, text="")
        #StartPage_display_text.pack(pady=10, padx=10)         Meter O OK se for 200

        
        button = tk.Button(self, text="Go Back", command=lambda:[delete_text_brige(),master.show_frame(PageBridges)])
        button.pack()

class PageBridges_intefaces_Editar(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        
        label = tk.Label(self, text="Name of the Brige para editar:")
        label.pack(pady=10, padx=10)

        global Brige_Name_Text_Get
        Brige_Name_Text_Get = tk.Text(self,height = 1, width = 20)
        Brige_Name_Text_Get.pack()

        label = tk.Label(self, text="New Name of the Brige para editar:")
        label.pack(pady=10, padx=10)

        global Brige_Name_Text_Edit
        Brige_Name_Text_Edit = tk.Text(self,height = 1, width = 20)
        Brige_Name_Text_Edit.pack()

        
        button_Submit_Brige_Edit = tk.Button(self, text="Submit", command=Editar_intefaces_Bridge)
        button_Submit_Brige_Edit.pack(pady=5, padx=10)

        #global StartPage_display_text
        #StartPage_display_text = tk.Label(self, text="")
        #StartPage_display_text.pack(pady=10, padx=10)         Meter O OK se for 200

        
        button = tk.Button(self, text="Go Back", command=lambda:[delete_text_brige_edit(),master.show_frame(PageBridges)])
        button.pack()

class PageBridges_intefaces_Delete(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        
        label = tk.Label(self, text="Name of the Brige para Apagar:")
        label.pack(pady=10, padx=10)

        global Brige_Name_Text_Get_Delete
        Brige_Name_Text_Get_Delete = tk.Text(self,height = 1, width = 20)
        Brige_Name_Text_Get_Delete.pack()
        
        button_Submit_Brige_Delete = tk.Button(self, text="Submit", command=Delete_intefaces_Bridge)
        button_Submit_Brige_Delete.pack(pady=5, padx=10)

        #global StartPage_display_text
        #StartPage_display_text = tk.Label(self, text="")
        #StartPage_display_text.pack(pady=10, padx=10)         Meter O OK se for 200

        
        button = tk.Button(self, text="Go Back", command=lambda:[delete_text_brige_delete(),master.show_frame(PageBridges)])
        button.pack()

#---------PORTS

class PageBridges_Port_inteface_List(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        
        label = tk.Label(self, text="This page is for list all BRIGE PORTS")
        label.pack(pady=10, padx=10)

        button_listar_Bridge_ports = tk.Button(self, text='List all brige ports', command=listar_Bridge_Ports)
        button_listar_Bridge_ports.pack()

        global response_label_bridge_ports
        response_label_bridge_ports = tk.Text(self)
        response_label_bridge_ports.pack()

        
        button = tk.Button(self, text="Go Back", command=lambda:[delete_text_brige_Ports(),master.show_frame(PageBridges)])
        button.pack()


class PageBridges_Port_inteface_Create(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        
        label = tk.Label(self, text="Name of the Interface:")
        label.pack(pady=10, padx=10)

        global Port_Interface_Name_Text
        Port_Interface_Name_Text = tk.Text(self,height = 1, width = 20)
        Port_Interface_Name_Text.pack()


        label = tk.Label(self, text="Name of the Brige:")
        label.pack(pady=10, padx=10)

        global Port_Brige_Name_Text
        Port_Brige_Name_Text = tk.Text(self,height = 1, width = 20)
        Port_Brige_Name_Text.pack()

        
        button_Submit_Brige_Port = tk.Button(self, text="Submit", command=submit_Brige_Port)
        button_Submit_Brige_Port.pack()
        
        button = tk.Button(self, text="Go Back", command=lambda:[delete_text_brige(),master.show_frame(PageBridges)])
        button.pack()


class PageBridges_Port_inteface_Patch(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        
        label = tk.Label(self, text="Name of the Interface:")
        label.pack(pady=10, padx=10)

        global Port_Interface_Name_Text_Patch
        Port_Interface_Name_Text_Patch = tk.Text(self,height = 1, width = 20)
        Port_Interface_Name_Text_Patch.pack()


        label = tk.Label(self, text="Name of the Brige:")
        label.pack(pady=10, padx=10)

        global Port_Brige_Name_Text_Patch
        Port_Brige_Name_Text_Patch = tk.Text(self,height = 1, width = 20)
        Port_Brige_Name_Text_Patch.pack()

        
        button_Submit_Brige_Port_Patch = tk.Button(self, text="Submit", command=Submit_Brige_Port_Patch)
        button_Submit_Brige_Port_Patch.pack()
        
        button = tk.Button(self, text="Go Back", command=lambda:[delete_text_brige_Ports_Patch(),master.show_frame(PageBridges)])
        button.pack()

class PageBridges_Port_inteface_Delete(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        
        label = tk.Label(self, text="Name of the Interface para Apagar:")
        label.pack(pady=10, padx=10)

        global Interface_Name_Text_Get_Delete
        Interface_Name_Text_Get_Delete = tk.Text(self,height = 1, width = 20)
        Interface_Name_Text_Get_Delete.pack()
        
        button_Submit_Brige_Delete_Port = tk.Button(self, text="Submit", command=Delete_intefaces_Bridge_Port)
        button_Submit_Brige_Delete_Port.pack(pady=5, padx=10)

        #global StartPage_display_text
        #StartPage_display_text = tk.Label(self, text="")
        #StartPage_display_text.pack(pady=10, padx=10)         Meter O OK se for 200

        
        button = tk.Button(self, text="Go Back", command=lambda:[delete_text_brige_Port_delete(),master.show_frame(PageBridges)])
        button.pack()


class PageWireless_Redes(tk.Frame):
    def __init__(self, master):
        super().__init__(master)       

        button = tk.Button(self, text="Ativar rede Wireless", command=lambda:[delete_text_wireless(),master.show_frame(PageWireless_Redes_Ativar)])
        button.pack()

        button = tk.Button(self, text="Desativar rede Wireless", command=lambda:[delete_text_wireless(),master.show_frame(PageWireless_Redes_Desativar)])
        button.pack()

        button = tk.Button(self, text="Configurar rede Wireless", command=lambda:[delete_text_wireless(),master.show_frame(PageWireless_Redes_Configurar)])
        button.pack()

        button = tk.Button(self, text="Go to Start Page", command=lambda:[delete_text_wireless(),master.show_frame(StartPage)])
        button.pack()


#-------------------------------Security-profiles

class PageSecurityProfiles(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        

        button = tk.Button(self, text="Create security-profile", command=lambda:[master.show_frame(PageSecurityProfiles_Put)])
        button.pack()

        button = tk.Button(self, text="Patch security-profile", command=lambda:[master.show_frame(PageSecurityProfiles_Patch)])
        button.pack()

        button = tk.Button(self, text="Delete security-profile", command=lambda:[master.show_frame(PageSecurityProfiles_Delete)])
        button.pack()

        button = tk.Button(self, text="Go to Start Page", command=lambda:[master.show_frame(StartPage)])
        button.pack()

class PageSecurityProfiles_Put(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        
        label = tk.Label(self, text="Name of the security-profile:")
        label.pack(pady=10, padx=10)

        global Security_Profile_Name_Text
        Security_Profile_Name_Text = tk.Text(self,height = 1, width = 20)
        Security_Profile_Name_Text.pack()

        label = tk.Label(self, text="Authentication-type of the security-profile:")
        label.pack(pady=10, padx=10)

        global Authentication_Type_Text
        Authentication_Type_Text = tk.Text(self,height = 1, width = 20)
        Authentication_Type_Text.pack()
        
        button_Submit_Security_Profiles = tk.Button(self, text="Submit", command=submit_SecurityProfile)
        button_Submit_Security_Profiles.pack(pady=5, padx=10)

        #global StartPage_display_text
        #StartPage_display_text = tk.Label(self, text="")
        #StartPage_display_text.pack(pady=10, padx=10)         Meter O OK se for 200

        
        button = tk.Button(self, text="Go Back", command=lambda:[delete_text_security_profiles_put(),master.show_frame(PageSecurityProfiles)])
        button.pack()

class PageSecurityProfiles_Patch(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        
        label = tk.Label(self, text="Name of the security-profile to patch:")
        label.pack(pady=10, padx=10)

        global Security_Profile_Name_Text_To_Patch
        Security_Profile_Name_Text_To_Patch = tk.Text(self,height = 1, width = 20)
        Security_Profile_Name_Text_To_Patch.pack()


        label = tk.Label(self, text="Name of the new security-profile:")
        label.pack(pady=10, padx=10)

        global Port_Brige_Name_Text_Patch
        Port_Brige_Name_Text_Patch = tk.Text(self,height = 1, width = 20)
        Port_Brige_Name_Text_Patch.pack()

        
        button_Submit_Brige_Port_Patch = tk.Button(self, text="Submit", command=Submit_Security_Profile_Patch)
        button_Submit_Brige_Port_Patch.pack()
        
        button = tk.Button(self, text="Go Back", command=lambda:[delete_Security_Profile_Patch(),master.show_frame(PageSecurityProfiles)])
        button.pack()


class PageSecurityProfiles_Delete(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        
        label = tk.Label(self, text="Name of the security-profile to Delete:")
        label.pack(pady=10, padx=10)

        global Security_Profile_Name_Text_To_Delete
        Security_Profile_Name_Text_To_Delete = tk.Text(self,height = 1, width = 20)
        Security_Profile_Name_Text_To_Delete.pack()
     
        button_Submit_Brige_Port_Delete = tk.Button(self, text="Submit", command=Submit_Security_Profile_Delete)
        button_Submit_Brige_Port_Delete.pack()
        
        button = tk.Button(self, text="Go Back", command=lambda:[delete_Security_Profile_Delete(),master.show_frame(PageSecurityProfiles)])
        button.pack()

#________________WIRELESS_REDE

class PageWireless_Redes_Ativar(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        
        label = tk.Label(self, text="Name of the wireless network:")
        label.pack(pady=10, padx=10)

        global Wireless_Name_Text
        Wireless_Name_Text = tk.Text(self,height = 1, width = 20)
        Wireless_Name_Text.pack()
        
        button_Submit_Brige_Port_Patch = tk.Button(self, text="Submit", command=Submit_Wireless_Redes_Ativar)
        button_Submit_Brige_Port_Patch.pack()
        
        button = tk.Button(self, text="Go Back", command=lambda:[delete_PageWireless_Redes_Ativar(),master.show_frame(PageWireless_Redes)])
        button.pack()

class PageWireless_Redes_Desativar(tk.Frame):

    def __init__(self, master):
        super().__init__(master)
        
        label = tk.Label(self, text="Name of the wireless network:")
        label.pack(pady=10, padx=10)

        global Wireless_Name_Text_Desativar
        Wireless_Name_Text_Desativar = tk.Text(self,height = 1, width = 20)
        Wireless_Name_Text_Desativar.pack()
        
        button_Submit_Brige_Port_Patch = tk.Button(self, text="Submit", command=Submit_Wireless_Redes_Desativar)
        button_Submit_Brige_Port_Patch.pack()
        
        button = tk.Button(self, text="Go Back", command=lambda:[delete_PageWireless_Redes_Desativar(),master.show_frame(PageWireless_Redes)])
        button.pack()

class PageWireless_Redes_Configurar(tk.Frame):

    def __init__(self, master):
        super().__init__(master)

        label = tk.Label(self, text="Name of the wireless network:")
        label.pack(pady=10, padx=10)

        global Wireless_Name_Text_Name
        Wireless_Name_Text_Name = tk.Text(self,height = 1, width = 20)
        Wireless_Name_Text_Name.pack()
        
        label = tk.Label(self, text="Mode of the wireless network:")
        label.pack(pady=10, padx=10)

        global Wireless_Name_Text_Mode
        Wireless_Name_Text_Mode = tk.Text(self,height = 1, width = 20)
        Wireless_Name_Text_Mode.pack()

        label = tk.Label(self, text="SSID of the wireless network:")
        label.pack(pady=10, padx=10)

        global Wireless_Name_Text_SSID
        Wireless_Name_Text_SSID = tk.Text(self,height = 1, width = 20)
        Wireless_Name_Text_SSID.pack()


        label = tk.Label(self, text="Security Profile of the wireless network:")
        label.pack(pady=10, padx=10)

        global Wireless_Name_Text_Security_Profile
        Wireless_Name_Text_Security_Profile = tk.Text(self,height = 1, width = 20)
        Wireless_Name_Text_Security_Profile.pack()


        
        button_Submit_Brige_Port_Patch = tk.Button(self, text="Submit", command=Submit_Wireless_Redes_Configurar)
        button_Submit_Brige_Port_Patch.pack()
        
        button = tk.Button(self, text="Go Back", command=lambda:[delete_PageWireless_Redes_Configurar(),master.show_frame(PageWireless_Redes)])
        button.pack()

#___________static routes

class PageStatic_routes(tk.Frame):
    def __init__(self, master):
        super().__init__(master)       

        button = tk.Button(self, text="List static routes", command=lambda:[master.show_frame(PageStatic_routes_Listar)])
        button.pack()

        button = tk.Button(self, text="Create static route", command=lambda:[master.show_frame(PageStatic_routes_Criar)])
        button.pack()

        button = tk.Button(self, text="Edit static route", command=lambda:[master.show_frame(PageStatic_routes_Editar)])
        button.pack()

        button = tk.Button(self, text="Delete static route", command=lambda:[master.show_frame(PageStatic_routes_Apagar)])
        button.pack()

        button = tk.Button(self, text="Go to Start Page", command=lambda:[master.show_frame(StartPage)])
        button.pack()


class PageStatic_routes_Listar(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        button_listar_Rostas_Estaticas = tk.Button(self, text='Listar todas as Rotas Estaticas', command=listar_Rotas_Estaticas)
        button_listar_Rostas_Estaticas.pack()

        global Response_Label_Rotas_Estaticas
        Response_Label_Rotas_Estaticas = tk.Text(self)
        Response_Label_Rotas_Estaticas.pack()

        
        button = tk.Button(self, text="Go Back", command=lambda:[Delete_Text_PageStatic_Routes_Listar(),master.show_frame(PageStatic_routes)])
        button.pack()

class PageStatic_routes_Criar(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        
        label = tk.Label(self, text="Dst. Adress:")
        label.pack(pady=10, padx=10)

        global Static_routes_Dst_Adress_Text
        Static_routes_Dst_Adress_Text = tk.Text(self,height = 1, width = 20)
        Static_routes_Dst_Adress_Text.pack()

        label = tk.Label(self, text="Gateway:")
        label.pack(pady=10, padx=10)

        global Static_routes_Gateway_Text
        Static_routes_Gateway_Text = tk.Text(self,height = 1, width = 20)
        Static_routes_Gateway_Text.pack()
        
        button_Submit_Security_Profiles = tk.Button(self, text="Submit", command=submit_PageStatic_routes_Criar)
        button_Submit_Security_Profiles.pack(pady=5, padx=10)

        
        button = tk.Button(self, text="Go Back", command=lambda:[delete_PageStatic_routes_Criar(),master.show_frame(PageStatic_routes)])
        button.pack()

class PageStatic_routes_Editar(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        
        label = tk.Label(self, text="ID of the reoute list:")
        label.pack(pady=10, padx=10)

        global PageStatic_routes_Editar_Id_Text
        PageStatic_routes_Editar_Id_Text = tk.Text(self,height = 1, width = 20)
        PageStatic_routes_Editar_Id_Text.pack()

        label = tk.Label(self, text="New Name of the Dst. Adress:")
        label.pack(pady=10, padx=10)

        global PageStatic_routes_Editar_Dst_Adress_Text
        PageStatic_routes_Editar_Dst_Adress_Text = tk.Text(self,height = 1, width = 20)
        PageStatic_routes_Editar_Dst_Adress_Text.pack()

        label = tk.Label(self, text="New Name of the Gateway:")
        label.pack(pady=10, padx=10)

        global PageStatic_routes_Editar_Gateway_Text
        PageStatic_routes_Editar_Gateway_Text = tk.Text(self,height = 1, width = 20)
        PageStatic_routes_Editar_Gateway_Text.pack()

        
        button_Submit_Brige_Edit = tk.Button(self, text="Submit", command=submit_PageStatic_routes_Editar)
        button_Submit_Brige_Edit.pack(pady=5, padx=10)

        button = tk.Button(self, text="Go Back", command=lambda:[delete_PageStatic_routes_Editar(),master.show_frame(PageStatic_routes)])
        button.pack()

class PageStatic_routes_Apagar(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        
        label = tk.Label(self, text="ID da rota para Apagar:")
        label.pack(pady=10, padx=10)

        global Static_routes_Apagar_ID_Text
        Static_routes_Apagar_ID_Text = tk.Text(self,height = 1, width = 20)
        Static_routes_Apagar_ID_Text.pack()
        
        button_Submit_Brige_Delete_Port = tk.Button(self, text="Submit", command=Submit_PageStatic_Delete)
        button_Submit_Brige_Delete_Port.pack(pady=5, padx=10)

        button = tk.Button(self, text="Go Back", command=lambda:[PageStatic_routes_Apagar_delete(),master.show_frame(PageStatic_routes)])
        button.pack()


##__________________ip address

class PageIp_Address(tk.Frame):
    def __init__(self, master):
        super().__init__(master)       

        button = tk.Button(self, text="Listar endreços Ip", command=lambda:[master.show_frame(PageIp_Address_Listar)])
        button.pack()

        button = tk.Button(self, text="Criar endreços Ip", command=lambda:[master.show_frame(PageIp_Address_Criar)])
        button.pack()

        button = tk.Button(self, text="Editar endreços Ip", command=lambda:[master.show_frame(PageIp_Address_Editar)])
        button.pack()

        button = tk.Button(self, text="Apagar endreços Ip", command=lambda:[master.show_frame(PageIp_Address_Apagar)])
        button.pack()

        button = tk.Button(self, text="Go to Start Page", command=lambda:[master.show_frame(StartPage)])
        button.pack()

class PageIp_Address_Listar(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        button_listar_Ip_Address = tk.Button(self, text='Listar endreços Ip', command=listar_Ip_Address)
        button_listar_Ip_Address.pack()

        global Response_Label_Rotas_Estaticas
        Response_Label_Rotas_Estaticas = tk.Text(self)
        Response_Label_Rotas_Estaticas.pack()

        
        button = tk.Button(self, text="Go Back", command=lambda:[Delete_Text_PageIp_Address_Listar(),master.show_frame(PageIp_Address)])
        button.pack()

class PageIp_Address_Criar(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        
        label = tk.Label(self, text="Adress:")
        label.pack(pady=10, padx=10)

        global PageIp_Address_Criar_Adress_Text
        PageIp_Address_Criar_Adress_Text = tk.Text(self,height = 1, width = 20)
        PageIp_Address_Criar_Adress_Text.pack()

        label = tk.Label(self, text="Network:")
        label.pack(pady=10, padx=10)

        global PageIp_Address_Criar_Network_Text
        PageIp_Address_Criar_Network_Text = tk.Text(self,height = 1, width = 20)
        PageIp_Address_Criar_Network_Text.pack()

        label = tk.Label(self, text="Interface:")
        label.pack(pady=10, padx=10)

        global PageIp_Address_Criar_Interface_Text
        PageIp_Address_Criar_Interface_Text = tk.Text(self,height = 1, width = 20)
        PageIp_Address_Criar_Interface_Text.pack()
        
        button_Submit_Security_Profiles = tk.Button(self, text="Submit", command=submit_PageIp_Address_Criar)
        button_Submit_Security_Profiles.pack(pady=5, padx=10)

        
        button = tk.Button(self, text="Go Back", command=lambda:[delete_PageIp_Address_Criar(),master.show_frame(PageIp_Address)])
        button.pack()


class PageIp_Address_Editar(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        
        label = tk.Label(self, text="ID:")
        label.pack(pady=10, padx=10)

        global PageIp_Address_Editar_Id_Text
        PageIp_Address_Editar_Id_Text = tk.Text(self,height = 1, width = 20)
        PageIp_Address_Editar_Id_Text.pack()

        label = tk.Label(self, text="Adress:")
        label.pack(pady=10, padx=10)

        global PageIp_Address_Editar_Adress_Text
        PageIp_Address_Editar_Adress_Text = tk.Text(self,height = 1, width = 20)
        PageIp_Address_Editar_Adress_Text.pack()

        label = tk.Label(self, text="Network")
        label.pack(pady=10, padx=10)

        global PageIp_Address_Editar_Network_Text
        PageIp_Address_Editar_Network_Text = tk.Text(self,height = 1, width = 20)
        PageIp_Address_Editar_Network_Text.pack()

        label = tk.Label(self, text="Interface:")
        label.pack(pady=10, padx=10)

        global PPageIp_Address_Editar_Interface_Text
        PPageIp_Address_Editar_Interface_Text = tk.Text(self,height = 1, width = 20)
        PPageIp_Address_Editar_Interface_Text.pack()

        
        button_Submit_Brige_Edit = tk.Button(self, text="Submit", command=submit_PageIp_Address_Editar)
        button_Submit_Brige_Edit.pack(pady=5, padx=10)

        button = tk.Button(self, text="Go Back", command=lambda:[delete_PageIp_Address_Editar(),master.show_frame(PageIp_Address)])
        button.pack()

class PageIp_Address_Apagar(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        
        label = tk.Label(self, text="ID:")
        label.pack(pady=10, padx=10)

        global PageIp_Address_Apagar_ID_Text
        PageIp_Address_Apagar_ID_Text = tk.Text(self,height = 1, width = 20)
        PageIp_Address_Apagar_ID_Text.pack()
        
        button_Submit_Brige_Delete_Port = tk.Button(self, text="Submit", command=Submit_PageIp_Address_Apagar)
        button_Submit_Brige_Delete_Port.pack(pady=5, padx=10)

        button = tk.Button(self, text="Go Back", command=lambda:[PageIp_Address_Apagar_delete(),master.show_frame(PageIp_Address)])
        button.pack()

##__________________PageDHCP
class PageDHCP(tk.Frame):
    def __init__(self, master):
        super().__init__(master)       

        button = tk.Button(self, text="Listar DHCP", command=lambda:[master.show_frame(PageDHCP_Listar)])
        button.pack()

        button = tk.Button(self, text="Criar DHCP", command=lambda:[master.show_frame(PageDHCP_Criar)])
        button.pack()

        button = tk.Button(self, text="Editar DHCP", command=lambda:[master.show_frame(PageDHCP_Editar)])
        button.pack()

        button = tk.Button(self, text="Apagar DHCP", command=lambda:[master.show_frame(PageDHCP_Apagar)])
        button.pack()

        button = tk.Button(self, text="Go to Start Page", command=lambda:[master.show_frame(StartPage)])
        button.pack()

class PageDHCP_Listar(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        button_PageDHCP_Listar = tk.Button(self, text='Listar DHCP', command=listar_PageDHCP)
        button_PageDHCP_Listar.pack()

        global Response_PageDHCP_Listar
        Response_PageDHCP_Listar = tk.Text(self)
        Response_PageDHCP_Listar.pack()
  
        button = tk.Button(self, text="Go Back", command=lambda:[Delete_PageDHCP_Listar(),master.show_frame(PageDHCP)])
        button.pack()

class PageDHCP_Criar(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        
        label = tk.Label(self, text="Nome:")
        label.pack(pady=10, padx=10)

        global PageDHCP_Criar_Nome_Text
        PageDHCP_Criar_Nome_Text = tk.Text(self,height = 1, width = 20)
        PageDHCP_Criar_Nome_Text.pack()

        label = tk.Label(self, text="Interface:")
        label.pack(pady=10, padx=10)

        global PageDHCP_Criar_Interface_Text
        PageDHCP_Criar_Interface_Text = tk.Text(self,height = 1, width = 20)
        PageDHCP_Criar_Interface_Text.pack()
        
        button_Submit_Security_Profiles = tk.Button(self, text="Submit", command=submit_PageDHCP_Criar)
        button_Submit_Security_Profiles.pack(pady=5, padx=10)

        
        button = tk.Button(self, text="Go Back", command=lambda:[delete_PageDHCP_Criar(),master.show_frame(PageDHCP)])
        button.pack()


class PageDHCP_Editar(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        label = tk.Label(self, text="ID:")
        label.pack(pady=10, padx=10)

        global PageDHCP_Editar_ID_Text
        PageDHCP_Editar_ID_Text = tk.Text(self,height = 1, width = 20)
        PageDHCP_Editar_ID_Text.pack()
        
        label = tk.Label(self, text="Name:")
        label.pack(pady=10, padx=10)

        global PageDHCP_Editar_Name_Text
        PageDHCP_Editar_Name_Text = tk.Text(self,height = 1, width = 20)
        PageDHCP_Editar_Name_Text.pack()

        label = tk.Label(self, text="Interface:")
        label.pack(pady=10, padx=10)

        global PageDHCP_Editar_Interface_Text
        PageDHCP_Editar_Interface_Text = tk.Text(self,height = 1, width = 20)
        PageDHCP_Editar_Interface_Text.pack()

        
        button_Submit_Brige_Edit = tk.Button(self, text="Submit", command=submit_PageDHCP_Editar)
        button_Submit_Brige_Edit.pack(pady=5, padx=10)

        button = tk.Button(self, text="Go Back", command=lambda:[delete_PageDHCP_Editar(),master.show_frame(PageDHCP)])
        button.pack()

class PageDHCP_Apagar(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        
        label = tk.Label(self, text="ID:")
        label.pack(pady=10, padx=10)

        global PageDHCP_Apagar_ID_Text
        PageDHCP_Apagar_ID_Text = tk.Text(self,height = 1, width = 20)
        PageDHCP_Apagar_ID_Text.pack()
        
        button_Submit_PageDHCP_Apagar = tk.Button(self, text="Submit", command=Submit_PageDHCP_Apagar)
        button_Submit_PageDHCP_Apagar.pack(pady=5, padx=10)

        button = tk.Button(self, text="Go Back", command=lambda:[delete_PageDHCP_Apagar(),master.show_frame(PageDHCP)])
        button.pack()

##__________________PageWirewall
class PageWirewall(tk.Frame):
    def __init__(self, master):
        super().__init__(master)       

        button = tk.Button(self, text="Listar Firewall", command=lambda:[master.show_frame(PageWirewall_Listar)])
        button.pack()

        button = tk.Button(self, text="Criar Firewall", command=lambda:[master.show_frame(PageWirewall_Criar)])
        button.pack()

        button = tk.Button(self, text="Editar Firewall", command=lambda:[master.show_frame(PageWirewall_Editar)])
        button.pack()

        button = tk.Button(self, text="Apagar Firewall", command=lambda:[master.show_frame(PageWirewall_Apagar)])
        button.pack()
        
        button = tk.Button(self, text="Go to Start Page", command=lambda:[master.show_frame(StartPage)])
        button.pack()

class PageWirewall_Listar(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        button_button_PageDHCP = tk.Button(self, text='Listar DHCP', command=listar_PageWirewall_Listar)
        button_button_PageDHCP.pack()

        global Response_PageWirewall_Listar
        Response_PageWirewall_Listar = tk.Text(self)
        Response_PageWirewall_Listar.pack()
  
        button = tk.Button(self, text="Go Back", command=lambda:[delete_PageWirewall_Listar(),master.show_frame(PageWirewall)])
        button.pack()

class PageWirewall_Criar(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        
        label = tk.Label(self, text="action:")
        label.pack(pady=10, padx=10)

        global PageWirewall_Criar_Action_Text
        PageWirewall_Criar_Action_Text = tk.Text(self,height = 1, width = 20)
        PageWirewall_Criar_Action_Text.pack()

        label = tk.Label(self, text="chain:")
        label.pack(pady=10, padx=10)

        global PageWirewall_Criar_Chain_Text
        PageWirewall_Criar_Chain_Text = tk.Text(self,height = 1, width = 20)
        PageWirewall_Criar_Chain_Text.pack()

        label = tk.Label(self, text="Disabled:")
        label.pack(pady=10, padx=10)

        global PageWirewall_Criar_Disabled_Text
        PageWirewall_Criar_Disabled_Text = tk.Text(self,height = 1, width = 20)
        PageWirewall_Criar_Disabled_Text.pack()

        label = tk.Label(self, text="src-address:")
        label.pack(pady=10, padx=10)

        global PageWirewall_Criar_Src_Address_Text
        PageWirewall_Criar_Src_Address_Text = tk.Text(self,height = 1, width = 20)
        PageWirewall_Criar_Src_Address_Text.pack()

        label = tk.Label(self, text="dst-address:")
        label.pack(pady=10, padx=10)

        global PageWirewall_Criar_Dst_Address_Text
        PageWirewall_Criar_Dst_Address_Text = tk.Text(self,height = 1, width = 20)
        PageWirewall_Criar_Dst_Address_Text.pack()
        
        button_Submit_Security_Profiles = tk.Button(self, text="Submit", command=submit_PageWirewall_Criar)
        button_Submit_Security_Profiles.pack(pady=5, padx=10)

        
        button = tk.Button(self, text="Go Back", command=lambda:[delete_PageWirewall_Criar(),master.show_frame(PageWirewall)])
        button.pack()

class PageWirewall_Editar(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        label = tk.Label(self, text="ID:")
        label.pack(pady=10, padx=10)

        global PageWirewall_Editar_ID_Text
        PageWirewall_Editar_ID_Text = tk.Text(self,height = 1, width = 20)
        PageWirewall_Editar_ID_Text.pack()
        
        label = tk.Label(self, text="action:")
        label.pack(pady=10, padx=10)

        global PageWirewall_Editar_Action_Text
        PageWirewall_Editar_Action_Text = tk.Text(self,height = 1, width = 20)
        PageWirewall_Editar_Action_Text.pack()

        label = tk.Label(self, text="chain:")
        label.pack(pady=10, padx=10)

        global PageWirewall_Editar_Chain_Text
        PageWirewall_Editar_Chain_Text = tk.Text(self,height = 1, width = 20)
        PageWirewall_Editar_Chain_Text.pack()

        label = tk.Label(self, text="Disabled:")
        label.pack(pady=10, padx=10)

        global PageWirewall_Editar_Disabled_Text
        PageWirewall_Editar_Disabled_Text = tk.Text(self,height = 1, width = 20)
        PageWirewall_Editar_Disabled_Text.pack()

        label = tk.Label(self, text="src-address:")
        label.pack(pady=10, padx=10)

        global PageWirewall_Editar_Src_Address_Text
        PageWirewall_Editar_Src_Address_Text = tk.Text(self,height = 1, width = 20)
        PageWirewall_Editar_Src_Address_Text.pack()

        label = tk.Label(self, text="dst-address:")
        label.pack(pady=10, padx=10)

        global PageWirewall_Editar_Dst_Address_Text
        PageWirewall_Editar_Dst_Address_Text = tk.Text(self,height = 1, width = 20)
        PageWirewall_Editar_Dst_Address_Text.pack()
        
        
        button_Submit_Firewall_Edit = tk.Button(self, text="Submit", command=submit_PageWirewall_Editar)
        button_Submit_Firewall_Edit.pack(pady=5, padx=10)

        button = tk.Button(self, text="Go Back", command=lambda:[delete_PageWirewall_Editar(),master.show_frame(PageWirewall)])
        button.pack()

class PageWirewall_Apagar(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        
        label = tk.Label(self, text="ID:")
        label.pack(pady=10, padx=10)

        global PageWirewall_Apagar_ID_Text
        PageWirewall_Apagar_ID_Text = tk.Text(self,height = 1, width = 20)
        PageWirewall_Apagar_ID_Text.pack()
        
        button_Submit_PageDHCP_Apagar = tk.Button(self, text="Submit", command=Submit_PageWirewall_Apagar)
        button_Submit_PageDHCP_Apagar.pack(pady=5, padx=10)

        button = tk.Button(self, text="Go Back", command=lambda:[delete_PageWirewall_Apagar(),master.show_frame(PageWirewall)])
        button.pack()

#___________DNS

class PageDNS(tk.Frame):
    def __init__(self, master):
        super().__init__(master)       

        button = tk.Button(self, text="Ativar DNS", command=lambda:[master.show_frame(PageDNS_Ativar)])
        button.pack()

        button = tk.Button(self, text="Desativar DNS", command=lambda:[master.show_frame(PageDNS_Desativar)])
        button.pack()

        button = tk.Button(self, text="Configurar DNS", command=lambda:[master.show_frame(PageDNS_Configurar)])
        button.pack()
        
        button = tk.Button(self, text="Go to Start Page", command=lambda:[master.show_frame(StartPage)])
        button.pack()

class PageDNS_Ativar(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        
        label = tk.Label(self, text="Ativar DNS")
        label.pack(pady=10, padx=10)

        
        button_Submit_Brige_Port_Patch = tk.Button(self, text="Ativar", command=Submit_PageDNS_Ativar)
        button_Submit_Brige_Port_Patch.pack()
        
        button = tk.Button(self, text="Go Back", command=lambda:[master.show_frame(PageDNS)])
        button.pack()

class PageDNS_Desativar(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        
        label = tk.Label(self, text="Desativar DNS")
        label.pack(pady=10, padx=10)

        
        button_Submit_Brige_Port_Patch = tk.Button(self, text="Desativar", command=Submit_PageDNS_Desativar)
        button_Submit_Brige_Port_Patch.pack()
        
        button = tk.Button(self, text="Go Back", command=lambda:[master.show_frame(PageDNS)])
        button.pack()  

class PageDNS_Configurar(tk.Frame):

    def __init__(self, master):
        super().__init__(master)

        label = tk.Label(self, text="DNS addresses:")
        label.pack(pady=10, padx=10)

        global PageDNS_Name_Text_Name
        PageDNS_Name_Text_Name = tk.Text(self,height = 1, width = 20)
        PageDNS_Name_Text_Name.pack()
        
        label = tk.Label(self, text="DoH Server:")
        label.pack(pady=10, padx=10)

        global PageDNS_Name_Text_DoH
        PageDNS_Name_Text_DoH = tk.Text(self,height = 1, width = 20)
        PageDNS_Name_Text_DoH.pack()

        button_Submit_Brige_Port_Patch = tk.Button(self, text="Submit", command=Submit_PageDNS_Configurar)
        button_Submit_Brige_Port_Patch.pack()
        
        button = tk.Button(self, text="Go Back", command=lambda:[delete_PageDNS_Configurar(),master.show_frame(PageDNS)])
        button.pack()



#___________ProtocoloEncaminhamento

class PageProtocoloEncaminhamento(tk.Frame):
    def __init__(self, master):
        super().__init__(master)       

        button = tk.Button(self, text="Criar Instância", command=lambda:[master.show_frame(PageProtocoloEncaminhamento_Criar_Instancia)])
        button.pack()

        button = tk.Button(self, text="Criar Area", command=lambda:[master.show_frame(PageProtocoloEncaminhamento_Criar_Area)])
        button.pack()

        button = tk.Button(self, text="Criar Interface Template", command=lambda:[master.show_frame(PageProtocoloEncaminhamento_Criar_Interface_Template)])
        button.pack()

        button = tk.Button(self, text="Ativar Interface Template", command=lambda:[master.show_frame(PageProtocoloEncaminhamento_Ativar)])
        button.pack()

        button = tk.Button(self, text="Desativar Interface Template", command=lambda:[master.show_frame(PageProtocoloEncaminhamento_Desativar)])
        button.pack()
        
        button = tk.Button(self, text="Go to Start Page", command=lambda:[master.show_frame(StartPage)])
        button.pack()

class PageProtocoloEncaminhamento_Criar_Instancia(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        
        label = tk.Label(self, text="Instance Name")
        label.pack(pady=10, padx=10)

        global PageProtocoloEncaminhamento_Criar_Instancia_Name
        PageProtocoloEncaminhamento_Criar_Instancia_Name = tk.Text(self,height = 1, width = 20)
        PageProtocoloEncaminhamento_Criar_Instancia_Name.pack()

        
        button_Submit_Instancia = tk.Button(self, text="Criar", command=Submit_PageProtocoloEncaminhamento_Criar_Instancia)
        button_Submit_Instancia.pack()
        
        button = tk.Button(self, text="Go Back", command=lambda:[delete_PageProtocoloEncaminhamento_Criar_Instancia(), master.show_frame(PageProtocoloEncaminhamento)])
        button.pack()

class PageProtocoloEncaminhamento_Criar_Area(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        
        label = tk.Label(self, text="Area Name")
        label.pack(pady=10, padx=10)

        global PageProtocoloEncaminhamento_Criar_Area_Name
        PageProtocoloEncaminhamento_Criar_Area_Name = tk.Text(self,height = 1, width = 20)
        PageProtocoloEncaminhamento_Criar_Area_Name.pack()

        label = tk.Label(self, text="Instance Name")
        label.pack(pady=10, padx=10)

        global PageProtocoloEncaminhamento_Criar_Area_Instancia_Name
        PageProtocoloEncaminhamento_Criar_Area_Instancia_Name = tk.Text(self,height = 1, width = 20)
        PageProtocoloEncaminhamento_Criar_Area_Instancia_Name.pack()

        label = tk.Label(self, text="Area ID")
        label.pack(pady=10, padx=10)

        global PageProtocoloEncaminhamento_Criar_Area_ID
        PageProtocoloEncaminhamento_Criar_Area_ID = tk.Text(self,height = 1, width = 20)
        PageProtocoloEncaminhamento_Criar_Area_ID.pack()

        
        button_Submit_Instancia = tk.Button(self, text="Criar", command=Submit_PageProtocoloEncaminhamento_Criar_Area)
        button_Submit_Instancia.pack()
        
        button = tk.Button(self, text="Go Back", command=lambda:[delete_PageProtocoloEncaminhamento_Criar_Area(), master.show_frame(PageProtocoloEncaminhamento)])
        button.pack()

class PageProtocoloEncaminhamento_Criar_Interface_Template(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        
        label = tk.Label(self, text="Area name")
        label.pack(pady=10, padx=10)

        global PageProtocoloEncaminhamento_Criar_Interface_Template_Area_Name
        PageProtocoloEncaminhamento_Criar_Interface_Template_Area_Name = tk.Text(self,height = 1, width = 20)
        PageProtocoloEncaminhamento_Criar_Interface_Template_Area_Name.pack()

        
        button_Submit_Instancia = tk.Button(self, text="Criar", command=Submit_PageProtocoloEncaminhamento_Interface_Template)
        button_Submit_Instancia.pack()
        
        button = tk.Button(self, text="Go Back", command=lambda:[delete_PageProtocoloEncaminhamento_Criar_Interface_Template(), master.show_frame(PageProtocoloEncaminhamento)])
        button.pack()

class PageProtocoloEncaminhamento_Ativar(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        
        label = tk.Label(self, text="Instance name")
        label.pack(pady=10, padx=10)
        
        global PageProtocoloEncaminhamento_Ativar_Instancia
        PageProtocoloEncaminhamento_Ativar_Instancia = tk.Text(self,height = 1, width = 20)
        PageProtocoloEncaminhamento_Ativar_Instancia.pack()
        
        button_Submit_Instancia = tk.Button(self, text="Ativar", command=Submit_PageProtocoloEncaminhamento_Ativar)
        button_Submit_Instancia.pack()
        
        button = tk.Button(self, text="Go Back", command=lambda:[delete_PageProtocoloEncaminhamento_Ativar_Instancia(), master.show_frame(PageProtocoloEncaminhamento)])
        button.pack()

class PageProtocoloEncaminhamento_Desativar(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        
        label = tk.Label(self, text="Instance name")
        label.pack(pady=10, padx=10)

        global PageProtocoloEncaminhamento_Desativar_Instancia
        PageProtocoloEncaminhamento_Desativar_Instancia = tk.Text(self,height = 1, width = 20)
        PageProtocoloEncaminhamento_Desativar_Instancia.pack()

        
        button_Submit_Instancia = tk.Button(self, text="Desativar", command=Submit_PageProtocoloEncaminhamento_Desativar)
        button_Submit_Instancia.pack()
        
        button = tk.Button(self, text="Go Back", command=lambda:[delete_PageProtocoloEncaminhamento_Desativar_Instancia(), master.show_frame(PageProtocoloEncaminhamento)])
        button.pack()

class PageVPN(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        
        
        label = tk.Label(self, text="IP Pool Name")
        label.pack(pady=10, padx=10)

        global PageVPN_Pool_Name
        PageVPN_Pool_Name = tk.Text(self,height = 1, width = 20)
        PageVPN_Pool_Name.pack()

        label = tk.Label(self, text="IP Pool Addresses")
        label.pack(pady=10, padx=10)
        
        global PageVPN_Pool_Addresses
        PageVPN_Pool_Addresses = tk.Text(self,height = 1, width = 20)
        PageVPN_Pool_Addresses.pack()

        
        label = tk.Label(self, text="PPP Profile Local Address")
        label.pack(pady=10, padx=10)
        
        global PageVPN_PPP_Profile_Local_Address
        PageVPN_PPP_Profile_Local_Address = tk.Text(self,height = 1, width = 20)
        PageVPN_PPP_Profile_Local_Address.pack()

        label = tk.Label(self, text="PPP Profile Remote Address")
        label.pack(pady=10, padx=10)
        
        global PageVPN_PPP_Profile_Remote_Address
        PageVPN_PPP_Profile_Remote_Address = tk.Text(self,height = 1, width = 20)
        PageVPN_PPP_Profile_Remote_Address.pack()

        label = tk.Label(self, text="PPP Secret Name")
        label.pack(pady=10, padx=10)
        
        global PageVPN_PPP_Secret_Name
        PageVPN_PPP_Secret_Name = tk.Text(self,height = 1, width = 20)
        PageVPN_PPP_Secret_Name.pack()


        label = tk.Label(self, text="PPP Secret Password")
        label.pack(pady=10, padx=10)
        
        global PageVPN_PPP_Secret_Password
        PageVPN_PPP_Secret_Password = tk.Text(self,height = 1, width = 20)
        PageVPN_PPP_Secret_Password.pack()

        label = tk.Label(self, text="L2TP Server IPsec Secret")
        label.pack(pady=10, padx=10)
        
        global PageVPN_L2TP_Server_IPsec_Secret
        PageVPN_L2TP_Server_IPsec_Secret = tk.Text(self,height = 1, width = 20)
        PageVPN_L2TP_Server_IPsec_Secret.pack()

        button_Submit_Instancia = tk.Button(self, text="Criar", command=Submit_PageVPN)
        button_Submit_Instancia.pack()
        
        button = tk.Button(self, text="Go Back", command=lambda:[delete_PageVPN(), master.show_frame(StartPage)])
        button.pack()

##FUNCOES--------------------------------------------------------------------------
def submit_text():
    """Update the display label with the entered text"""
    global ip
    ip = ip_Text.get("1.0","end-1c")
    user = user_Text.get("1.0","end-1c")
    password = password_Text.get("1.0","end-1c")
    global url
    url = "https://"+ user +":"+ password +"@"+ip+"/rest/"
    StartPage_display_text.config(text=url)
 


def submit_Brige():
    """Update the display label with the entered text"""
    global url

    Name = Brige_Name_Text.get("1.0","end-1c")
    payload = {"name": Name}
    json_payload = json.dumps(payload)
    headers = {"Content-Type": "application/json"}

    response = requests.put(url+"interface/bridge",headers=headers,data=json_payload,verify=False)
    response_data = response.json()

    print(response.status_code)




def listar_intefaces():
        
    global url

    response = requests.get(url+"interface",verify=False)
    response_data = response.json()

    devolver = ""
    for i in range(len(response_data)):
        #print("id: "+response_data[i]['.id'] +"  name: "+ response_data[i]['name'] )
        devolver = devolver + ("id: "+response_data[i]['.id'] +"  name: "+ response_data[i]['name']+"\n")
    print(devolver)


    response_label.delete('1.0', 'end')
    response_label.insert('end', devolver)

def delete_text():
    response_label.delete("1.0","end-1c")       

def listar_intefaces_wireless():
        
    global url
    response = requests.get(url+"interface/wireless",verify=False)
    response_data = response.json()

    devolver = ""
    for i in range(len(response_data)):
        #print("id: "+response_data[i]['.id'] +"  name: "+ response_data[i]['name'] )
        devolver = devolver + ("id: "+response_data[i]['.id'] +"  name: "+ response_data[i]['name']+"  disabled:  "+ response_data[i]['disabled']+"\n")

    response_label_wireless.delete('1.0', 'end')
    response_label_wireless.insert('end', devolver)

def delete_text_wireless():
    response_label_wireless.delete("1.0","end-1c")

def listar_intefaces_Bridge():
        
    global url
    response = requests.get(url+"interface/bridge",verify=False)
    response_data = response.json()

    devolver = ""
    for i in range(len(response_data)):
        #print("id: "+response_data[i]['.id'] +"  name: "+ response_data[i]['name'] )
        devolver = devolver + ("id: "+response_data[i]['.id'] +"  name: "+ response_data[i]['name']+"\n")

    response_label_bridges.delete('1.0', 'end')
    response_label_bridges.insert('end', devolver)

    
def delete_text_brige():
    response_label_bridges.delete("1.0","end-1c")


def Editar_intefaces_Bridge():     
    global url
    response = requests.get(url+"interface/bridge",verify=False)
    response_data = response.json()
    Name = Brige_Name_Text_Get.get("1.0","end-1c")
    #print(Name)
    ID_a_mudar = ""
    for i in range(len(response_data)):
        if response_data[i]['name'] == Name:
            ID_a_mudar = response_data[i]['.id']
            print(ID_a_mudar)

    Name = Brige_Name_Text_Edit.get("1.0","end-1c")
    payload = {"name": Name}
    json_payload = json.dumps(payload)
    headers = {"Content-Type": "application/json"}
    response = requests.patch(url+"interface/bridge/"+ID_a_mudar,headers=headers,data=json_payload,verify=False)
    response_data = response.json()
    print(response.status_code)


def delete_text_brige_edit():
    Brige_Name_Text_Get.delete("1.0","end-1c")
    Brige_Name_Text_Edit.delete("1.0","end-1c")


def Delete_intefaces_Bridge():     
    global url
    response = requests.get(url+"interface/bridge",verify=False)
    response_data = response.json()
    Name = Brige_Name_Text_Get_Delete.get("1.0","end-1c")
    ID_a_mudar = ""
    for i in range(len(response_data)):
        if response_data[i]['name'] == Name:
            ID_a_mudar = response_data[i]['.id']

    response = requests.delete(url+"interface/bridge/"+ID_a_mudar,verify=False)
    print(response.status_code)

def delete_text_brige_delete():
    Brige_Name_Text_Get_Delete.delete("1.0","end-1c")
 

#-----------PORTS

def listar_Bridge_Ports():
        
    global url
    response = requests.get(url+"interface/bridge/port",verify=False)
    response_data = response.json()

    devolver = ""
    for i in range(len(response_data)):
        #print("id: "+response_data[i]['.id'] +"  name: "+ response_data[i]['name'] )
        devolver = devolver + ("id: "+response_data[i]['.id'] +"  interface: "+ response_data[i]['interface']+"  bridge: "+ response_data[i]['bridge']+"\n")
        
    response_label_bridge_ports.delete('1.0', 'end')
    response_label_bridge_ports.insert('end', devolver)

def delete_text_brige_Ports():
    response_label_bridge_ports.delete("1.0","end-1c")

def submit_Brige_Port():
    """Update the display label with the entered text"""
    global url

    interface = Port_Interface_Name_Text.get("1.0","end-1c")
    bridge = Port_Brige_Name_Text.get("1.0","end-1c")

    payload = {"interface":interface,"bridge":bridge}
    json_payload = json.dumps(payload)
    headers = {"Content-Type": "application/json"}
    #print(interface +"  "+ bridge)

    response = requests.put(url+"interface/bridge/port",headers=headers,data=json_payload,verify=False)
    response_data = response.json()

    print(response.status_code)


def Submit_Brige_Port_Patch():
    """Update the display label with the entered text"""
    global url
    response = requests.get(url+"interface/bridge/port",verify=False)
    response_data = response.json()
    #print(response_data)

    interface = Port_Interface_Name_Text_Patch.get("1.0","end-1c")
    bridge = Port_Brige_Name_Text_Patch.get("1.0","end-1c")

    ID_a_mudar = ""
    for i in range(len(response_data)):
        if response_data[i]['interface'] == interface:
            ID_a_mudar = response_data[i]['.id']
            #print(ID_a_mudar)


    payload = {"bridge":bridge}
    json_payload = json.dumps(payload)
    headers = {"Content-Type": "application/json"}
    #print(interface +"  "+ bridge)

    response = requests.patch(url+"interface/bridge/port/"+ID_a_mudar,headers=headers,data=json_payload,verify=False)
    response_data = response.json()
    print(response.status_code)

def delete_text_brige_Ports_Patch():
    Port_Interface_Name_Text_Patch.delete("1.0","end-1c")
    Port_Brige_Name_Text_Patch.delete("1.0","end-1c")


def Delete_intefaces_Bridge_Port():     
    global url
    response = requests.get(url+"interface/bridge/port",verify=False)
    response_data = response.json()
    Name = Interface_Name_Text_Get_Delete.get("1.0","end-1c")
    ID_a_apagar = ""
    for i in range(len(response_data)):
        if response_data[i]['interface'] == Name:
            ID_a_apagar = response_data[i]['.id']
            print(ID_a_apagar)
            print(url+"interface/bridge/port"+ID_a_apagar)
    response = requests.delete(url+"interface/bridge/port/"+ID_a_apagar,verify=False)
    print(response.status_code)

def delete_text_brige_Port_delete():
    Interface_Name_Text_Get_Delete.delete("1.0","end-1c")
#______________security-profiles

def submit_SecurityProfile():
    """Update the display label with the entered text"""
    global url

    Name = Security_Profile_Name_Text.get("1.0","end-1c")
    Authentication_Type = Authentication_Type_Text.get("1.0","end-1c")
    print(Name)
    print(Authentication_Type)
   
    payload = {"name":Name,"authentication-types":Authentication_Type}
    json_payload = json.dumps(payload)
    headers = {"Content-Type": "application/json"}
    response = requests.put(url+"interface/wireless/security-profiles",headers=headers,data=json_payload,verify=False)
    response_data = response.json()
    print(response.status_code)

def delete_text_security_profiles_put():
    Security_Profile_Name_Text.delete("1.0","end-1c")
    Authentication_Type_Text.delete("1.0","end-1c")


def Submit_Security_Profile_Patch():
    """Update the display label with the entered text"""
    global url
    response = requests.get(url+"interface/wireless/security-profiles",verify=False)
    response_data = response.json()
    #print(response_data)

    Name_Text_To_Patch = Security_Profile_Name_Text_To_Patch.get("1.0","end-1c")
    Name_Text_Patch = Port_Brige_Name_Text_Patch.get("1.0","end-1c")

    ID_a_mudar = ""
    for i in range(len(response_data)):
        if response_data[i]['name'] == Name_Text_To_Patch:
            ID_a_mudar = response_data[i]['.id']
            print(ID_a_mudar)


    payload = {"name":Name_Text_Patch}
    json_payload = json.dumps(payload)
    headers = {"Content-Type": "application/json"}
    #print(interface +"  "+ bridge)

    response = requests.patch(url+"interface/wireless/security-profiles/"+ID_a_mudar,headers=headers,data=json_payload,verify=False)
    response_data = response.json()
    print(response.status_code)

def delete_Security_Profile_Patch():
    Security_Profile_Name_Text_To_Patch.delete("1.0","end-1c")
    Port_Brige_Name_Text_Patch.delete("1.0","end-1c")
    

def Submit_Security_Profile_Delete():     
    global url
    response = requests.get(url+"interface/wireless/security-profiles",verify=False)
    response_data = response.json()
    Name = Security_Profile_Name_Text_To_Delete.get("1.0","end-1c")
    ID_a_mudar = ""
    for i in range(len(response_data)):
        if response_data[i]['name'] == Name:
            ID_a_mudar = response_data[i]['.id']

    response = requests.delete(url+"interface/wireless/security-profiles/"+ID_a_mudar,verify=False)
    print(response.status_code)

def delete_Security_Profile_Delete():
    Security_Profile_Name_Text_To_Delete.delete("1.0","end-1c")


#_________WIRELESS REDE

def Submit_Wireless_Redes_Ativar():
    """Update the display label with the entered text"""
    global url
    response = requests.get(url+"interface/wireless",verify=False)
    response_data = response.json()
    #print(response_data)

    Name_Text_To_Patch = Wireless_Name_Text.get("1.0","end-1c")

    ID_a_mudar = ""
    for i in range(len(response_data)):
        if response_data[i]['name'] == Name_Text_To_Patch:
            ID_a_mudar = response_data[i]['.id']
            print(ID_a_mudar)

    payload = {"disabled":"no"}
    json_payload = json.dumps(payload)
    headers = {"Content-Type": "application/json"}
    response = requests.patch(url+"interface/wireless/"+ID_a_mudar,headers=headers,data=json_payload,verify=False)
    response_data = response.json()
    print(response.status_code)  

def delete_PageWireless_Redes_Ativar():
     Wireless_Name_Text.delete("1.0","end-1c")

def Submit_Wireless_Redes_Desativar():
    """Update the display label with the entered text"""
    global url
    response = requests.get(url+"interface/wireless",verify=False)
    response_data = response.json()
    #print(response_data)

    Name_Text_To_Patch = Wireless_Name_Text_Desativar.get("1.0","end-1c")

    ID_a_mudar = ""
    for i in range(len(response_data)):
        if response_data[i]['name'] == Name_Text_To_Patch:
            ID_a_mudar = response_data[i]['.id']
            print(ID_a_mudar)

    payload = {"disabled":"yes"}
    json_payload = json.dumps(payload)
    headers = {"Content-Type": "application/json"}
    response = requests.patch(url+"interface/wireless/"+ID_a_mudar,headers=headers,data=json_payload,verify=False)
    response_data = response.json()
    print(response.status_code) 

def delete_PageWireless_Redes_Desativar():
     Wireless_Name_Text_Desativar.delete("1.0","end-1c")


def Submit_Wireless_Redes_Configurar():
    """Update the display label with the entered text"""
    global url
    response = requests.get(url+"interface/wireless",verify=False)
    response_data = response.json()
    #print(response_data)
    
    Name_Text_Name = Wireless_Name_Text_Name.get("1.0","end-1c")
    Name_Text_Mode = Wireless_Name_Text_Mode.get("1.0","end-1c")
    Name_Text_SSID = Wireless_Name_Text_SSID.get("1.0","end-1c")
    Name_Text_Security_Profile = Wireless_Name_Text_Security_Profile.get("1.0","end-1c")

    ID_a_mudar = ""
    for i in range(len(response_data)):
        if response_data[i]['name'] == Name_Text_Name:
            ID_a_mudar = response_data[i]['.id']
            if Name_Text_Mode == "":
                Name_Text_Mode = response_data[i]['mode']
                print(Name_Text_Mode)
            if Name_Text_SSID == "":
                Name_Text_SSID = response_data[i]['ssid']
                print(Name_Text_SSID)
            if Name_Text_Security_Profile == "":
                Name_Text_Security_Profile = response_data[i]['security-profile']
                print(Name_Text_Security_Profile)

    payload = {"mode":Name_Text_Mode,"ssid":Name_Text_SSID,"security-profile":Name_Text_Security_Profile}
    json_payload = json.dumps(payload)
    headers = {"Content-Type": "application/json"}
    response = requests.patch(url+"interface/wireless/"+ID_a_mudar,headers=headers,data=json_payload,verify=False)
    response_data = response.json()
    print(response.status_code) 

def delete_PageWireless_Redes_Configurar():
     Wireless_Name_Text_Name.delete("1.0","end-1c")
     Wireless_Name_Text_Mode.delete("1.0","end-1c")
     Wireless_Name_Text_SSID.delete("1.0","end-1c")
     Wireless_Name_Text_Security_Profile.delete("1.0","end-1c")

def listar_Rotas_Estaticas():
        
    global url
    response = requests.get(url+"ip/route?static=yes",verify=False)
    response_data = response.json()
    #print(response_data)
    devolver = ""
    for i in range(len(response_data)):
        #print("id: "+response_data[i]['.id'] +"  name: "+ response_data[i]['name'] )
        devolver = devolver + ("id: "+response_data[i]['.id'] +"  dst-address: "+ response_data[i]['dst-address']+" gateway: "+response_data[i]['gateway']+" dynamic: "+response_data[i]['dynamic']+"\n")

    Response_Label_Rotas_Estaticas.delete('1.0', 'end')
    Response_Label_Rotas_Estaticas.insert('end', devolver)

def Delete_Text_PageStatic_Routes_Listar():
    Response_Label_Rotas_Estaticas.delete("1.0","end-1c")

def submit_PageStatic_routes_Criar():
    """Update the display label with the entered text"""
    global url

    Dst_Adress = Static_routes_Dst_Adress_Text.get("1.0","end-1c")
    Gateway = Static_routes_Gateway_Text.get("1.0","end-1c")
    
   
    payload = {"dst-address":Dst_Adress,"gateway":Gateway}
    json_payload = json.dumps(payload)
    headers = {"Content-Type": "application/json"}
    response = requests.put(url+"ip/route?static=yes",headers=headers,data=json_payload,verify=False)
    response_data = response.json()
    print(response.status_code)   

def delete_PageStatic_routes_Criar():
    Static_routes_Dst_Adress_Text.delete("1.0","end-1c")
    Static_routes_Gateway_Text.delete("1.0","end-1c")


def submit_PageStatic_routes_Editar():
    """Update the display label with the entered text"""
    global url
    response = requests.get(url+"ip/route?static=yes",verify=False)
    response_data = response.json()
    #print(response_data)
    
    Id_Text = PageStatic_routes_Editar_Id_Text.get("1.0","end-1c")
    Dst_Adress_Text = PageStatic_routes_Editar_Dst_Adress_Text.get("1.0","end-1c")
    Gateway_Text = PageStatic_routes_Editar_Gateway_Text.get("1.0","end-1c")

    ID_a_mudar = ""
    for i in range(len(response_data)):
        if response_data[i]['.id'] == Id_Text:
            ID_a_mudar = response_data[i]['.id']
            if Dst_Adress_Text == "":
                Dst_Adress_Text = response_data[i]['dst-address']
                print(Dst_Adress_Text)
            if Gateway_Text == "":
                Gateway_Text = response_data[i]['gateway']
                print(Gateway_Text)


    payload = {"dst-address":Dst_Adress_Text,"gateway":Gateway_Text}
    json_payload = json.dumps(payload)
    headers = {"Content-Type": "application/json"}
    response = requests.patch(url+"ip/route/"+ID_a_mudar+"?static=yes",headers=headers,data=json_payload,verify=False)
    response_data = response.json()
    print(response.status_code) 


def delete_PageStatic_routes_Editar():
    PageStatic_routes_Editar_Id_Text.delete("1.0","end-1c")
    PageStatic_routes_Editar_Dst_Adress_Text.delete("1.0","end-1c")
    PageStatic_routes_Editar_Gateway_Text.delete("1.0","end-1c")


def Submit_PageStatic_Delete():     
    global url
    ID_Text = Static_routes_Apagar_ID_Text.get("1.0","end-1c")
    response = requests.delete(url+"ip/route/"+ID_Text+"?static=yes",verify=False)
    response_data = response.json()
    print(response.status_code)

def PageStatic_routes_Apagar_delete():
    Static_routes_Apagar_ID_Text.delete("1.0","end-1c")
#_________________IPs
def listar_Ip_Address():
        
    global url
    response = requests.get(url+"ip/address",verify=False)
    response_data = response.json()
    #print(response_data)
    devolver = ""
    for i in range(len(response_data)):
        #print("id: "+response_data[i]['.id'] +"  name: "+ response_data[i]['name'] )
        devolver = devolver + ("id: "+response_data[i]['.id'] +"  interface: "+ response_data[i]['interface']+" address: "+response_data[i]['address']+" network: "+response_data[i]['network']+"\n")

    Response_Label_Rotas_Estaticas.delete('1.0', 'end')
    Response_Label_Rotas_Estaticas.insert('end', devolver)

def Delete_Text_PageIp_Address_Listar():
    Response_Label_Rotas_Estaticas.delete("1.0","end-1c")

def submit_PageIp_Address_Criar():
    global url
    Adress_Text = PageIp_Address_Criar_Adress_Text.get("1.0","end-1c")
    Network_Text = PageIp_Address_Criar_Network_Text.get("1.0","end-1c")
    Interface_Text = PageIp_Address_Criar_Interface_Text.get("1.0","end-1c")
    
    payload = {"address":Adress_Text,"network":Network_Text,"interface":Interface_Text}
    json_payload = json.dumps(payload)
    headers = {"Content-Type": "application/json"}
    response = requests.put(url+"ip/address",headers=headers,data=json_payload,verify=False)
    response_data = response.json()
    print(response.status_code)

def delete_PageIp_Address_Criar():
    PageIp_Address_Criar_Adress_Text.delete("1.0","end-1c")
    PageIp_Address_Criar_Network_Text.delete("1.0","end-1c")
    PageIp_Address_Criar_Interface_Text.delete("1.0","end-1c")


def submit_PageIp_Address_Editar():     
    global url
    response = requests.get(url+"ip/address",verify=False)
    response_data = response.json()
    #print(response_data)
    
    Id_Text = PageIp_Address_Editar_Id_Text.get("1.0","end-1c")
    Adress_Text = PageIp_Address_Editar_Adress_Text.get("1.0","end-1c")
    Network_Text = PageIp_Address_Editar_Network_Text.get("1.0","end-1c")
    Interface_Text = PPageIp_Address_Editar_Interface_Text.get("1.0","end-1c")

    ID_a_mudar = ""
    for i in range(len(response_data)):
        if response_data[i]['.id'] == Id_Text:
            ID_a_mudar = response_data[i]['.id']
            print(ID_a_mudar)
            if Adress_Text == "":
                Adress_Text = response_data[i]['address']
            print(Adress_Text)
            if Network_Text == "":
                Network_Text = response_data[i]['network']
            print(Network_Text)
            if Interface_Text == "":
                Interface_Text = response_data[i]['interface']
            print(Interface_Text)


    payload = {"address":Adress_Text,"network":Network_Text,"interface":Interface_Text}
    json_payload = json.dumps(payload)
    headers = {"Content-Type": "application/json"}
    response = requests.patch(url+"ip/address/"+ID_a_mudar,headers=headers,data=json_payload,verify=False)
    response_data = response.json()
    print(response.status_code) 

def delete_PageIp_Address_Editar():
    PageIp_Address_Editar_Id_Text.delete("1.0","end-1c")
    PageIp_Address_Editar_Adress_Text.delete("1.0","end-1c")
    PageIp_Address_Editar_Network_Text.delete("1.0","end-1c")
    PPageIp_Address_Editar_Interface_Text.delete("1.0","end-1c")

def Submit_PageIp_Address_Apagar():     
    global url
    ID_Text = PageIp_Address_Apagar_ID_Text.get("1.0","end-1c")
    response = requests.delete(url+"ip/address/"+ID_Text,verify=False)
    response_data = response.json()
    print(response.status_code)

def PageIp_Address_Apagar_delete():
    PageIp_Address_Apagar_ID_Text.delete("1.0","end-1c")


##______________________DHCP__________________________________


def listar_PageDHCP():
        
    global url
    response = requests.get(url+"ip/dhcp-server",verify=False)
    response_data = response.json()
    devolver = ""
    for i in range(len(response_data)):
        devolver = devolver + ("id: "+response_data[i]['.id'] +"  interface: "+ response_data[i]['interface']+" name: "+response_data[i]['name']+" disabled: "+response_data[i]['disabled']+"\n")

    Response_PageDHCP_Listar.delete('1.0', 'end')
    Response_PageDHCP_Listar.insert('end', devolver)

def Delete_PageDHCP_Listar():
    Response_PageDHCP_Listar.delete("1.0","end-1c")

def submit_PageDHCP_Criar():
    global url

    Nome_Text = PageDHCP_Criar_Nome_Text.get("1.0","end-1c")
    Interface_Text = PageDHCP_Criar_Interface_Text.get("1.0","end-1c")
    
    payload = {"name":Nome_Text,"interface":Interface_Text}
    json_payload = json.dumps(payload)
    headers = {"Content-Type": "application/json"}
    response = requests.put(url+"ip/dhcp-server",headers=headers,data=json_payload,verify=False)
    response_data = response.json()
    print(response.status_code)

def delete_PageDHCP_Criar():
    PageDHCP_Criar_Nome_Text.delete("1.0","end-1c")
    PageDHCP_Criar_Interface_Text.delete("1.0","end-1c")


def submit_PageDHCP_Editar():     
    global url
    response = requests.get(url+"ip/dhcp-server",verify=False)
    response_data = response.json()
    #print(response_data)

    Id_Text = PageDHCP_Editar_ID_Text.get("1.0","end-1c")
    Name_Text = PageDHCP_Editar_Name_Text.get("1.0","end-1c")
    Interface_Text = PageDHCP_Editar_Interface_Text.get("1.0","end-1c")

    for i in range(len(response_data)):
        if response_data[i]['.id'] == Id_Text:
            print(Id_Text)
            if Name_Text == "":
                Name_Text = response_data[i]['name']
            print(Name_Text)
            if Interface_Text == "":
                Interface_Text = response_data[i]['interface']
            print(Interface_Text)


    payload = {"name":Name_Text,"interface":Interface_Text}
    json_payload = json.dumps(payload)
    headers = {"Content-Type": "application/json"}
    response = requests.patch(url+"ip/dhcp-server/"+Id_Text,headers=headers,data=json_payload,verify=False)
    response_data = response.json()
    print(response.status_code) 

def delete_PageDHCP_Editar():
    PageDHCP_Editar_ID_Text.delete("1.0","end-1c")
    PageDHCP_Editar_Name_Text.delete("1.0","end-1c")
    PageDHCP_Editar_Interface_Text.delete("1.0","end-1c")


def Submit_PageDHCP_Apagar():     
    global url
    ID_Text = PageDHCP_Apagar_ID_Text.get("1.0","end-1c")
    response = requests.delete(url+"ip/dhcp-server/"+ID_Text,verify=False)
    response_data = response.json()
    print(response.status_code)

def delete_PageDHCP_Apagar():
    PageDHCP_Apagar_ID_Text.delete("1.0","end-1c")

#---------------------FIREWALL

def listar_PageWirewall_Listar():
        
    global url
    response = requests.get(url+"ip/firewall/filter",verify=False)
    response_data = response.json()
    devolver = ""
    for i in range(len(response_data)):
        devolver = devolver + ("id:"+response_data[i]['.id'] +"  action:"+ response_data[i]['action']+" src-address:"+response_data[i]['src-address']+" chain:"+response_data[i]['chain']+"\n")

    Response_PageWirewall_Listar.delete('1.0', 'end')
    Response_PageWirewall_Listar.insert('end', devolver)

def delete_PageWirewall_Listar():
    Response_PageWirewall_Listar.delete("1.0","end-1c")


def submit_PageWirewall_Criar():
    global url
    
    Action_Text = PageWirewall_Criar_Action_Text.get("1.0","end-1c")
    Chain_Text = PageWirewall_Criar_Chain_Text.get("1.0","end-1c")
    Disabled_Text = PageWirewall_Criar_Disabled_Text.get("1.0","end-1c")
    Src_Address_Text = PageWirewall_Criar_Src_Address_Text.get("1.0","end-1c")
    Dst_Address_Text = PageWirewall_Criar_Dst_Address_Text.get("1.0","end-1c")
    
    payload = {"action":Action_Text,"chain":Chain_Text,"disabled":Disabled_Text,"src-address":Src_Address_Text,"dst-address":Dst_Address_Text}
    json_payload = json.dumps(payload)
    headers = {"Content-Type": "application/json"}
    response = requests.put(url+"ip/firewall/filter",headers=headers,data=json_payload,verify=False)
    response_data = response.json()
    print(response.status_code)

def delete_PageWirewall_Criar():
    PageWirewall_Criar_Action_Text.delete("1.0","end-1c")
    PageWirewall_Criar_Chain_Text.delete("1.0","end-1c")
    PageWirewall_Criar_Disabled_Text.delete("1.0","end-1c")
    PageWirewall_Criar_Src_Address_Text.delete("1.0","end-1c")
    PageWirewall_Criar_Dst_Address_Text.delete("1.0","end-1c")

def submit_PageWirewall_Editar():     
    global url
    response = requests.get(url+"ip/firewall/filter",verify=False)
    response_data = response.json()
    #print(response_data)

    ID_Text = PageWirewall_Editar_ID_Text.get("1.0","end-1c")
    Action_Text = PageWirewall_Editar_Action_Text.get("1.0","end-1c")
    Chain_Text = PageWirewall_Editar_Chain_Text.get("1.0","end-1c")
    Disabled_Text = PageWirewall_Editar_Disabled_Text.get("1.0","end-1c")
    Src_Address_Text = PageWirewall_Editar_Src_Address_Text.get("1.0","end-1c")
    Dst_Address_Text = PageWirewall_Editar_Dst_Address_Text.get("1.0","end-1c")

    for i in range(len(response_data)):
        if response_data[i]['.id'] == ID_Text:
            print(ID_Text)
            if Action_Text == "":
                Action_Text = response_data[i]['action']
            print(Action_Text)
            if Chain_Text == "":
                Chain_Text = response_data[i]['chain']
            print(Chain_Text)
            if Disabled_Text == "":
                Disabled_Text = response_data[i]['disabled']
            print(Disabled_Text)
            if Src_Address_Text == "":
                Src_Address_Text = response_data[i]['src-address']
            print(Src_Address_Text)
            if Dst_Address_Text == "":
                Dst_Address_Text = response_data[i]['dst-address']
            print(Dst_Address_Text)


    payload = {"action":Action_Text,"chain":Chain_Text,"disabled":Disabled_Text,"src-address":Src_Address_Text,"dst-address":Dst_Address_Text}
    json_payload = json.dumps(payload)
    headers = {"Content-Type": "application/json"}
    response = requests.patch(url+"ip/firewall/filter/"+ID_Text,headers=headers,data=json_payload,verify=False)
    response_data = response.json()
    print(response.status_code) 


def delete_PageWirewall_Editar():
    PageWirewall_Editar_ID_Text.delete("1.0","end-1c")
    PageWirewall_Editar_Action_Text.delete("1.0","end-1c")
    PageWirewall_Editar_Chain_Text.delete("1.0","end-1c")
    PageWirewall_Editar_Disabled_Text.delete("1.0","end-1c")
    PageWirewall_Editar_Src_Address_Text.delete("1.0","end-1c")
    PageWirewall_Editar_Dst_Address_Text.delete("1.0","end-1c")

def Submit_PageWirewall_Apagar():     
    global url
    ID_Text = PageWirewall_Apagar_ID_Text.get("1.0","end-1c")
    response = requests.delete(url+"ip/firewall/filter/"+ID_Text,verify=False)
    response_data = response.json()
    print(response.status_code)

def delete_PageWirewall_Apagar():
    PageWirewall_Apagar_ID_Text.delete("1.0","end-1c")


def Submit_PageDNS_Ativar():
    """Update the display label with the entered text"""
    global url
    
    payload = {"allow-remote-requests":"false",
               "servers":"8.8.8.8,1.1.1.1"}
    json_payload = json.dumps(payload)
    headers = {"Content-Type": "application/json"}
    response = requests.post(url+"ip/dns/set",headers=headers,data=json_payload,verify=False)
    response_data = response.json()
    print(response.status_code)

def Submit_PageDNS_Desativar():
    """Update the display label with the entered text"""
    global url
    
    payload = {"allow-remote-requests":"false",
               "servers":""}
    json_payload = json.dumps(payload)
    headers = {"Content-Type": "application/json"}
    response = requests.post(url+"ip/dns/set",headers=headers,data=json_payload,verify=False)
    response_data = response.json()
    print(response.status_code)

def Submit_PageDNS_Configurar():
    """Update the display label with the entered text"""
    global url
    response = requests.get(url+"ip/dns",verify=False)
    response_data = response.json()
    #print(response_data)
    
    Name_Text_servers = PageDNS_Name_Text_Name.get("1.0","end-1c")
    Name_Text_DoH = PageDNS_Name_Text_DoH.get("1.0","end-1c")
    
    if response_data['servers'] == "":
            Name_Text_servers = response_data['servers']
            print(Name_Text_servers)
            
    if Name_Text_DoH == "":
            Name_Text_DoH = response_data['use-doh-server']
            print(Name_Text_DoH)

    payload = {"servers":Name_Text_servers,"use-doh-server":Name_Text_DoH}
    json_payload = json.dumps(payload)
    headers = {"Content-Type": "application/json"}
    response = requests.post(url+"ip/dns/set",headers=headers,data=json_payload,verify=False)
    response_data = response.json()
    print(response.status_code)

def delete_PageDNS_Configurar():
    PageDNS_Name_Text_Name.delete("1.0","end-1c")
    PageDNS_Name_Text_DoH.delete("1.0","end-1c")

def Submit_PageProtocoloEncaminhamento_Criar_Instancia():
    """Update the display label with the entered text"""
    global url
    Instancia_Name = PageProtocoloEncaminhamento_Criar_Instancia_Name.get("1.0","end-1c")

    payload = {"name": Instancia_Name}
    json_payload = json.dumps(payload)
    headers = {"Content-Type": "application/json"}
    response = requests.post(url+"routing/ospf/instance/add",headers=headers,data=json_payload,verify=False)
    response_data = response.json()
    print(response_data)
    print(response.status_code)

def delete_PageProtocoloEncaminhamento_Criar_Instancia():
    PageProtocoloEncaminhamento_Criar_Instancia_Name.delete("1.0","end-1c")
    

def Submit_PageProtocoloEncaminhamento_Criar_Area():
    """Update the display label with the entered text"""
    global url
    Area_Name = PageProtocoloEncaminhamento_Criar_Area_Name.get("1.0","end-1c")
    Instancia_Name = PageProtocoloEncaminhamento_Criar_Area_Instancia_Name.get("1.0","end-1c")
    Area_ID = PageProtocoloEncaminhamento_Criar_Area_ID.get("1.0","end-1c")

    payload = {"name": Area_Name,
               "area-id": Area_ID,
               "instance": Instancia_Name}
    
    json_payload = json.dumps(payload)
    headers = {"Content-Type": "application/json"}
    response = requests.post(url+"routing/ospf/area/add",headers=headers,data=json_payload,verify=False)
    response_data = response.json()
    print(response_data)
    print(response.status_code)

def delete_PageProtocoloEncaminhamento_Criar_Area():
    PageProtocoloEncaminhamento_Criar_Area_Name.delete("1.0","end-1c")
    PageProtocoloEncaminhamento_Criar_Area_Instancia_Name.delete("1.0","end-1c")
    PageProtocoloEncaminhamento_Criar_Area_ID.delete("1.0","end-1c")

def Submit_PageProtocoloEncaminhamento_Interface_Template():
    """Update the display label with the entered text"""
    global url
    Area_Name = PageProtocoloEncaminhamento_Criar_Interface_Template_Area_Name.get("1.0","end-1c")

    payload = {"area": Area_Name}
    
    json_payload = json.dumps(payload)
    headers = {"Content-Type": "application/json"}
    response = requests.post(url+"routing/ospf/interface-template/add",headers=headers,data=json_payload,verify=False)
    response_data = response.json()
    print(response_data)
    print(response.status_code)

def delete_PageProtocoloEncaminhamento_Criar_Interface_Template():
    PageProtocoloEncaminhamento_Criar_Interface_Template_Area_Name.delete("1.0","end-1c")

def Submit_PageProtocoloEncaminhamento_Ativar():
    """Update the display label with the entered text"""
    global url
    response = requests.get(url+"routing/ospf/instance",verify=False)
    response_data = response.json()
    #print(response_data)

    Name_Text_To_Patch = PageProtocoloEncaminhamento_Ativar_Instancia.get("1.0","end-1c")

    ID_a_mudar = ""
    for i in range(len(response_data)):
        if response_data[i]['name'] == Name_Text_To_Patch:
            ID_a_mudar = response_data[i]['.id']
            print(ID_a_mudar)

    payload = {"disabled":"false"}
    json_payload = json.dumps(payload)
    headers = {"Content-Type": "application/json"}
    response = requests.patch(url+"routing/ospf/instance/"+ID_a_mudar,headers=headers,data=json_payload,verify=False)
    response_data = response.json()
    print(response.status_code)  

def delete_PageProtocoloEncaminhamento_Ativar_Instancia():
    PageProtocoloEncaminhamento_Ativar_Instancia.delete("1.0","end-1c")

def Submit_PageProtocoloEncaminhamento_Desativar():
    """Update the display label with the entered text"""
    global url
    response = requests.get(url+"routing/ospf/instance",verify=False)
    response_data = response.json()
    #print(response_data)

    Name_Text_To_Patch = PageProtocoloEncaminhamento_Desativar_Instancia.get("1.0","end-1c")

    ID_a_mudar = ""
    for i in range(len(response_data)):
        if response_data[i]['name'] == Name_Text_To_Patch:
            ID_a_mudar = response_data[i]['.id']
            print(ID_a_mudar)

    payload = {"disabled":"true"}
    json_payload = json.dumps(payload)
    headers = {"Content-Type": "application/json"}
    response = requests.patch(url+"routing/ospf/instance/"+ID_a_mudar,headers=headers,data=json_payload,verify=False)
    response_data = response.json()
    print(response.status_code)  

def delete_PageProtocoloEncaminhamento_Desativar_Instancia():
    PageProtocoloEncaminhamento_Desativar_Instancia.delete("1.0","end-1c")

def Submit_PageVPN():
    """Update the display label with the entered text"""
    
    #print(response_profile_data)

    #Make Pool
    Pool_Name = PageVPN_Pool_Name.get("1.0","end-1c")
    Pool_Addresses = PageVPN_Pool_Addresses.get("1.0","end-1c")

    payload = {"name": Pool_Name,
               "ranges":Pool_Addresses}
    json_payload = json.dumps(payload)
    headers = {"Content-Type": "application/json"}
    response = requests.post(url+"ip/pool/add",headers=headers,data=json_payload,verify=False)
    response_data = response.json()
    print(response.status_code)

    #Patch PPP Profile "default-encryption"

    PPP_Profile_Local = PageVPN_PPP_Profile_Local_Address.get("1.0","end-1c")
    PPP_Profile_Remote = PageVPN_PPP_Profile_Remote_Address.get("1.0","end-1c")

    payload = {"local-address": PPP_Profile_Local,
               "remote-address": PPP_Profile_Remote}
    json_payload = json.dumps(payload)
    headers = {"Content-Type": "application/json"}
    response_profile = requests.patch(url+"ppp/profile/*FFFFFFFE",headers=headers,data=json_payload,verify=False)
    response_data = response_profile.json()
    print(response_profile.status_code)

    #Make Secret 
    PPP_Secret_Name = PageVPN_PPP_Secret_Name.get("1.0","end-1c")
    PPP_Secret_Password = PageVPN_PPP_Secret_Password.get("1.0","end-1c")


    payload = {"name": PPP_Secret_Name,
               "password": PPP_Secret_Password,
               "profile": "default-encryption",
               "service": "l2tp"}
    json_payload = json.dumps(payload)
    headers = {"Content-Type": "application/json"}
    response_profile = requests.post(url+"ppp/secret/add",headers=headers,data=json_payload,verify=False)
    response_data = response_profile.json()
    print(response_profile.status_code)

    #Enable IPsec 
    IPsec_Secret = PageVPN_L2TP_Server_IPsec_Secret.get("1.0","end-1c")

    payload = {"enabled": "true",
               "ipsec-secret": IPsec_Secret,
               "authentication": "chap,mschap1,mschap2",
               "use-ipsec": "required",
               "default-profile": "default-encryption"}
    json_payload = json.dumps(payload)
    headers = {"Content-Type": "application/json"}
    response_profile = requests.post(url+"interface/l2tp-server/server/set",headers=headers,data=json_payload,verify=False)
    response_profile_data = response_profile.json()
    print(response_profile.status_code)

    
    payload = {"chain": "input",
               "protocol": "ipsec-esp",
               "action": "accept"}
    json_payload = json.dumps(payload)
    headers = {"Content-Type": "application/json"}
    response_profile = requests.post(url+"ip/firewall/filter/add",headers=headers,data=json_payload,verify=False)
    response_profile_data = response_profile.json()
    print(response_profile.status_code)


    payload = {"chain": "input",
               "protocol": "udp",
               "port": "1701,500,4500",
               "action": "accept"}
    json_payload = json.dumps(payload)
    headers = {"Content-Type": "application/json"}
    response_profile = requests.post(url+"ip/firewall/filter/add",headers=headers,data=json_payload,verify=False)
    response_profile_data = response_profile.json()
    print(response_profile.status_code)



def delete_PageVPN():
    PageVPN_L2TP_Server_IPsec_Secret.delete("1.0","end-1c")
    PageVPN_Pool_Addresses.delete("1.0","end-1c")
    PageVPN_Pool_Name.delete("1.0","end-1c")
    PageVPN_PPP_Profile_Local_Address.delete("1.0","end-1c")
    PageVPN_PPP_Profile_Remote_Address.delete("1.0","end-1c")
    PageVPN_PPP_Secret_Name.delete("1.0","end-1c")
    PageVPN_PPP_Secret_Password.delete("1.0","end-1c")
#__________________________________________________________________________________________________


if __name__ == "__main__":
    app = MyApp()
    app.mainloop()

