#! /bin/bash
cd
touch info.txt
echo -n 'Число и время: ' >> /home/anna/info.txt | date >> /home/anna/info.txt
echo -n 'Имя текущего пользователя: ' >> /home/anna/info.txt | hostname >> /home/anna/info.txt
echo -n 'Операционная система: ' >> /home/anna/info.txt | grep '^NAME' /etc/os-release >> /home/anna/info.txt
echo -n 'Кол-во папок в домашней директории: ' >> /home/anna/info.txt | ls -1d */ | wc -l >> /home/anna/info.txt
echo -n 'Общее количество файлов: ' >> /home/anna/info.txt | find . -type f | wc -l >> /home/anna/info.txt
