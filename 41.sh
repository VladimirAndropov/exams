#!/bin/bash

for file in "$@"; do
    echo "Обработка файла: $file"
    filetype=$(file -b "$file")
    
    case "$filetype" in
        *gzip*)
            echo "Разархивация файла с помощью gunzip..."
            gunzip -k "$file"
            ;;
        *bzip2*)
            echo "Разархивация файла с помощью bunzip2..."
            bunzip2 -k "$file"
            ;;
        *Zip*)
            echo "Разархивация файла с помощью unzip..."
            unzip "$file"
            ;;
        *compress*)
            echo "Разархивация файла с помощью uncompress..."
            uncompress "$file"
            ;;
        *tar*)
            echo "Разархивация файла с помощью tar..."
            tar -xf "$file"
            ;;
        *)
            echo "Файл '$file' не является поддерживаемым архивом. Пропускаем..."
            ;;
    esac
done

