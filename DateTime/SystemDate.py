# -*- coding: UTF-8 -*-

from datetime import datetime
from datetime import date
import re

class SystemDate(object):
    #----------------------------------------------------------------------
    @staticmethod
    def strtodate(pdate):
        """convert string to date in format YYYY-MM-DD
        :param  pdate: Date
        :rtype  DateTime"""
        #return datetime.strptime(str(date), '%Y-%m-%d').date()
        day = 0
        month = 0
        year = 0

        if '-' in pdate:
            (day, month, year) = str(pdate).split('-')
        elif '/'in pdate:
            (day, month, year) = str(pdate).split('/')

        if len(year) == 4:
            pdate = '%s/%s/%s' % (day, month, year)
            return datetime.strptime(pdate, '%d/%m/%Y').date()
        else :
            pdate = '%s/%s/%s' % (year, month, day)
            return datetime.strptime(pdate, '%d/%m/%Y').date()


    #----------------------------------------------------------------------
    @staticmethod
    def datetostr(pdate):
        """convert date to string in format DD/MM/YYYY
        :rtype  String
        :param pdate  Date"""
        return pdate.strftime('%d/%m/%Y')

    #----------------------------------------------------------------------
    @staticmethod
    def adddays(pdate, pdays):
        """add days on date
        :param pdate date
        :param pdays num days to add"""
        return date.fromordinal(pdate.toordinal() + pdays)

    #----------------------------------------------------------------------
    @staticmethod
    def removedays(pdate, pdays):
        """Remove days on date
        :param pdate: date
        :param pdays: num days to remove"""
        return date.fromordinal(pdate.toordinal() - pdays)

    #----------------------------------------------------------------------
    @staticmethod
    def getname(pdate, ptype='D'):
        """day of week name or month name
        :param pdate: date
        :param ptype: return type 'D' -> Day of week name 'M' -> Month name 'DMY' -> Day month and year names"""
        if ptype.upper() == 'D':
            return ['Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado', 'Domingo' ][pdate.weekday()]
        elif ptype.upper() == 'M':
            return ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho','Julho','Agosto', 'Setembro', 'Outubro','Novembro','Dezembro'][pdate.month-1]
        elif ptype.upper() == 'DMY':
            return '%s, %s de %s de %s' % (SystemDate.getname(pdate, 'D'), pdate.day, SystemDate.getname(pdate, 'M'), pdate.year)
        else:
            return ''

    #----------------------------------------------------------------------
    @staticmethod
    def getdatenow():
        """takes the current date"""
        return date.today()

    #----------------------------------------------------------------------
    @staticmethod
    def isweekday(pdate):
        """checks whether the day is a weekday"""
        if pdate.weekday() == 0 or pdate.weekday() == 6:
            return False
        else:
            return True

    #----------------------------------------------------------------------
    @staticmethod
    def isvaliddate(pdate):
        """Checks whether date is valid"""
        rex = re.compile(r'^(((0[1-9]|[12][0-9]|3[01])[- /.](0[13578]|1[02])|(0[1-9]|[12][0-9]|30)[- /.](0[469]|11)|(0[1-9]|1\d|2[0-8])[- /.]02)[- /.]\d{4}|29[- /.]02[- /.](\d{2}(0[48]|[2468][048]|[13579][26])|([02468][048]|[1359][26])00))$')
        return rex.match(str(pdate))