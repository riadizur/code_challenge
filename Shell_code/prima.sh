#!/bin/bash

# Menerima input bilangan dari argumen command line
bilangan=$1

# Array DB bilangan prima
prime=()

# Fungsi untuk mengecek apakah bilangan prima
is_prime(){
    local number=$1
    for (( i=0; i<=number; i++ )); do
        find_prime $i
        if [[ $? -eq 0 ]]; then
            prime+=($i) #Jika bilangan itu bilangan prima tapi bukan bilangan yang di tanyakan simpan ke array DB Prima
            if ((i == number)); then
                return 0 #Jika bilangan itu adalah bilangan prima dan bilangan yang di tanyakan
            fi
        fi
    done
    return 1
}

#Menemukan bilangan prima lain sebelum bilangan yang di tanyakan
find_prime() {
    local number=$1
    if ((number <= 1));then
        return 1 #Bukan bilangan prima
    fi
    n_prime=${#prime[@]}
    for ((j=0; j<n_prime; j++)); do
        if ((number % prime[j] == 0)); then # Nilai yang ditanyakan dibagi dengan bilangan prima yg ditemukan sebelumnya
            return 1 # Bukan bilangan prima
        fi
    done
    return 0 # Bilangan prima
}

# Memanggil fungsi is_prime dengan argumen bilangan
is_prime $bilangan

# Memeriksa hasil dari fungsi is_prime dan menampilkan output yang sesuai
if [[ $? -eq 0 ]]; then
    echo "bilangan ini adalah bilangan prima"
else
    echo "bilangan ini bukan bilangan prima"
fi
# echo "${prime[@]}" # Buat mengecek isi bilangan prima yang ditemukan