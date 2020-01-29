# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    installer.sh                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ythomas <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/04 10:03:37 by ythomas           #+#    #+#              #
#    Updated: 2019/11/09 12:38:03 by ythomas          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/bin/bash

PATH_INSTALLER="Miniconda3.sh"
FOLDER="/goinfre/Miniconda3/"

if [ $1 = "install" ]; then
	if [ ! -d $FOLDER ]; then
		echo "***   Creation du dossier   ***";
		sh $PATH_INSTALLER -p "$FOLDER";
	else
		echo "already installed";
	fi
elif [ $1 = "remove" ]; then
	if [ -d $FOLDER ]; then
		rm -rf $FOLDER;
		echo "$FOLDER is now deleted";
	else
		echo "Folder does not exist";
	fi
else
	echo "Unknow command";
fi
