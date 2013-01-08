#!/usr/bin/python
# -*- coding: utf-8 -*-

# Iniciado el martes 03/10/2012 por la tarde

# TAREAS
# Pensar en un ancho de las columnas parametizable
# listado de subcuentas limitado a un numero de filas
# Elección de empresa y año fiscal
# Número de asiento y fecha FALTA EN CABECERA

import os, time
from collections import OrderedDict

SUBS = {}

SUBS['4300001'] = {'Nombre':'Pepito Perez',
                'Debe':50.00,
                'Haber':20.00,
                'Saldo':30.00}

SUBS['4300002'] = {'Nombre':'Rodolfo Valentino',
                'Debe':50.00,
                'Haber':20.00,
                'Saldo':30.00}

SUBS['4300003'] = {'Nombre':'Agapito Bello',
                'Debe':50.00,
                'Haber':20.00,
                'Saldo':30.00}

SUBS['4300004'] = {'Nombre':'La Bella Donna',
                'Debe':50.00,
                'Haber':20.00,
                'Saldo':30.00}

SUBS['4300005'] = {'Nombre':'Tu madre',
                'Debe':50.00,
                'Haber':20.00,
                'Saldo':30.00}

                
SUBS['5720001'] = {'Nombre':'B.Santander',
                'Debe':100.00,
                'Haber':50.00,
                'Saldo':50.00}

SUBS['5720000'] = {'Nombre':'Bancos',
                'Debe':100.00,
                'Haber':50.00,
                'Saldo':50.00}

#EMPRESAS = [('PackardBell', (2010, 2011, 2012), 'andreas corp', (2011, 2012)]

AFISCAL = 2012
EMPRESA = 'andreas corporation inc.'

ASIEN = {}
Cuenta = ' '
Desc = ''
Debe = 0.00
Haber = 0.00
Saldo = 0.00

# DEFS

def cls():
    os.system('clear')

def topMost():
    print(chr(27) + "[0;44m")
    cls()
    print('ContaPlux (c) andreas 2012, Empresa: %s Año: %s' % ('{:<43}'.format(EMPRESA), str(AFISCAL)))
    print('=========================================================================================', end = "")
    print(chr(27) + "[0;44m")
    

def mostrar_Menu():
    topMost()
    print('[1] Asientos  [2] Subcuentas  [3] Listados  [4] Configuración  [7] Empresa  [0] Salir :', end = "")
    return input()

def mostrar_Asientos(msg = 'NOPARAR'): #se podría usar types.NoneType pero así no importo types
    topMost()
    if not Cuenta in SUBS:
        print(' ' * 60 + 'Asiento Saldo: ' + '{:>14.2f}'.format(Saldo))
    else:
        print('{:<7}'.format(Cuenta) + ' ' + '{:<20}'.format(SUBS[Cuenta]['Nombre']) + ' Saldo: ' + '{:>14.2f}'.format(SUBS[Cuenta]['Saldo']) + '          Asiento Saldo: ' + '{:>14,.2f}'.format(Saldo))
    print('Cuenta  Nombre               Descripción                    Debe           Haber         ')
    print('------- -------------------- ------------------------------ -------------- --------------')
    for na in ASIEN:
        print('{:<7}'.format(ASIEN[na]['Cuenta']) + ' ' + '{:<20}'.format(ASIEN[na]['Nombre']) + ' ' + '{:<30}'.format(ASIEN[na]['Descrip']) + ' ' + '{:>14,.2f}'.format(ASIEN[na]['Debe']) + ' ' + '{:>14,.2f}'.format(ASIEN[na]['Haber']))
    if msg != 'NOPARAR':
        return input(msg)

def listar_Cuentas(SubCta):
    lista = OrderedDict(sorted(SUBS.items(), key = lambda x: x[0]))
    print('------- --------------------')
    for i in lista:
        if SubCta == i[:len(SubCta)]:
            print('%s %s' % (i, SUBS[i]['Nombre']))
    print('')
    a = input('Nº.de Cuenta o Intro: ')
    if a != '':
        topMost()
        mostrar_Asientos()
        print(a)
        return valida_Cuenta(a)
        
def listar_Nombres(SubCta):
    lista = OrderedDict(sorted(SUBS.items(), key = lambda x: x[0]))
    print('------- --------------------')
    for i in lista:
        if SubCta.upper() in SUBS[i]['Nombre'].upper():
            print('%s %s' % (i, SUBS[i]['Nombre']))
    print('')
    a = input('Nº.de Cuenta o Intro: ')
    if a != '':
        topMost()
        mostrar_Asientos()
        print(a)
        return valida_Cuenta(a)

def valida_Cuenta(SubCta):
    if SubCta.replace('.', '').isdigit() or SubCta == '.': #solo son números o números con algún punto o un punto
        a = SubCta.split('.')
        if len(a) > 1: #había al menos un punto
            if a[1] != '': #43.1
                return a[0] + a[1].rjust(7 - len(a[0]), '0')
            else: #43.
                return listar_Cuentas(a[0])
        return listar_Cuentas(a[0]) #43
    else: #es un nombre de cuenta
        return listar_Nombres(SubCta)

def lista_Subcuentas():
    print('Cuenta  Nombre               Debe           Haber          Saldo')
    print('------- -------------------- -------------- -------------- --------------')
    lista = OrderedDict(sorted(SUBS.items(), key = lambda x: x[0]))
    for i in lista:
        print('{:<7}'.format(i) + ' ' + '{:<20}'.format(SUBS[i]['Nombre']) + ' ' + '{:>14,.2f}'.format(SUBS[i]['Debe']) + ' ' + '{:>14,.2f}'.format(SUBS[i]['Haber']) + ' ' + '{:>14,.2f}'.format(SUBS[i]['Saldo']))
    print('')
    return input('Seleccione Subcuenta: ')
    
def queSalida():
    print('')
    print(' [0] Cancelar listado')
    print('')
    print(' [1] Salida por pantalla')
    print(' [2] Salida por impresora')
    print(' [3] Salida a fichero')
    print('')
    return input('Seleccione la salida: ')


# ###################################################################
# INICIO
# ###################################################################


print(chr(27) + "[0;44m")
cls()
FLASH = '''

 ________________________________________________________________________________________
 ____,o888888o.________,o888888o._____b._____________8_8888888_8888888888___.8.__________
 ___8888_____`88.___._8888_____`88.___888o.__________8_______8_8888________.888._________
 ,8_8888_______`8._,8_8888_______`8b__Y88888o._______8_______8_8888_______:88888.________
 88_8888___________88_8888________`8b_.`Y888888o.____8_______8_8888______._`88888._______
 88_8888___________88_8888_________88_8o._`Y888888o._8_______8_8888_____.8._`88888.______
 88_8888___________88_8888_________88_8`Y8o._`Y88888o8_______8_8888____.8`8._`88888._____
 88_8888___________88_8888________,8P_8___`Y8o._`Y8888_______8_8888___.8'_`8._`88888.____
 `8_8888_______.8'_`8_8888_______,8P__8______`Y8o._`Y8_______8_8888__.8'___`8._`88888.`__
 ___8888_____,88'___`_8888_____,88'___8_________`Y8o.`_______8_8888_.888888888._`88888.__
 ____`8888888P'________`8888888P'_____8____________`Yo_______8_8888.8'_______`8._`88888._
 ___________________________________________PLUX__(XFREEDOM_GROUP_6nndemal6c6xinct.onion)
'''

#comentar las dos líneas siguientes para quitar la intro
print(FLASH)
time.sleep(1)
    
Menu = ''

while (Menu) != '0':

    Menu = mostrar_Menu()

    if Menu == '1': # ASIENTOS

        ASIEN = {}
        Cuenta = ' '
        Desc = ''
        Debe = 0.00
        Haber = 0.00
        Saldo = 0.00
        running = True
        resp = ''
        
        while (running):
        
            linea = ''
            if resp == '':
                Cuenta = mostrar_Asientos('')
            else:
                Cuenta = resp
                resp = ''
        
            if Cuenta != '':
                Cuenta = valida_Cuenta(Cuenta)
                if Cuenta in SUBS:
                    linea = Cuenta + ' ' + '{:<20}'.format(SUBS[Cuenta]['Nombre']) + ' '
                    resp = mostrar_Asientos(linea + 'Otra Cta.?: ')
                    if resp == '':
                        Desc = mostrar_Asientos(linea)
                        if Desc == '' and len(ASIEN) > 0:
                            Desc = ASIEN[len(ASIEN)]['Descrip']
                        linea = linea + '{:<30}'.format(Desc) + ' '
                        valor = mostrar_Asientos(linea)
                        if not valor.replace('-','').replace('.', '', 1).isdigit(): #tema de la coma
                            Debe = 0.00
                            linea = linea + '{:>14.2f}'.format(0) + ' '
                            valor = mostrar_Asientos(linea)
                            if valor.replace('-','').replace('.', '', 1).isdigit():
                                Haber = round(float(valor), 2)
                        else:
                            Debe = round(float(valor), 2)
                            Haber = 0.00
        
                        if Debe != 0.00 or Haber != 0.00:
                            nid = len(ASIEN) + 1
                            ASIEN[nid] = {'Cuenta':Cuenta, 'Nombre':SUBS[Cuenta]['Nombre'], 'Descrip':Desc, 'Debe':Debe, 'Haber':Haber}
                            Saldo = Saldo + Debe - Haber
                            Debe, Haber = 0.00, 0.00
                      
               
            else:
                seguir = ''
                if Saldo == 0.00:
                    if len(ASIEN) > 0:
                        seguir = input('¿Grabar el asiento? (S/N): ')
                        if seguir == '' or seguir.upper() =='S':
                            print('Grabando datos....')
                            time.sleep(1)
                            ASIEN = {}
                            Cuenta = ' '
                            Desc = ''
                            Debe = 0.00
                            Haber = 0.00
                            Saldo = 0.00
                            resp = ''
                    else:
                        running = False
                else:
                    seguir = input('¿Anular asiento en curso? (S/N): ')
                    if seguir.upper() == 'S':
                        break
                        
    elif Menu == '2': #Subcuentas
        topMost()
        lista_Subcuentas()
            
    elif Menu == '3': #Listados
        a = ''
        while a != '0':
            topMost()
            print('Listados disponibles:')
            print('')
            print(' [0] Volver al menú principal')
            print('')
            print(' [1] Listado de Diario')
            print(' [2] Listado de Mayor')
            print(' [3] Listado de Balances')
            print(' [4] Facturas Recibidas')
            print(' [5] Facturas Emitidas')
            print(' [6] Listado 347')
            print('')
            a = input('Seleccione listado: ')
            b, c = '', ''
            if a == '1':
                print('Listado de Diario')
                print('')
                input('')
            if a == '2':
                print('Listado de Mayor')
                print('')
                input('')
            if a == '3':
                while b != '0':
                    topMost()
                    print('Listado de Balances')
                    print('')
                    print(' [0] Volver a Listados')
                    print('')
                    print(' [1] Sumas y Saldos')
                    print(' [2] Pérdidas y Ganancias')
                    print(' [3] De Situación')
                    print('')
                    b = input('Seleccione listado: ')
                    topMost()
                    if b == '1':
                        print('Listado del Balance de Sumas y Saldos')
                        c = queSalida() #imprimir listado según b y c
                    elif b == '2':
                        print('Listado del Balance de Pérdidas y Ganancias')
                        c = queSalida() #imprimir listado según b y c
                    elif b == '3':
                        print('Listado del Balance de Situación')
                        c = queSalida() #imprimir listado según b y c

            if a == '4':
                print('Facturas Recibidas')
                print('')
                input('')
            if a == '5':
                print('Facturas Emitidas')
                print('')
                input('')
            if a == '6':
                print('Listado 347')
                print('')
                input('')
    elif Menu == '4': #Configuración
        pass
    elif Menu == '7': #Empresas
        pass
print(chr(27) + "[0;39m")
cls()

