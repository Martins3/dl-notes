//
// Created by martin on 17-12-28.

#include <unistd.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <time.h>
#include <dirent.h>
#include <pwd.h>
#include <stdio.h>
#include <stdlib.h>
#include <grp.h>
#include <string>
#include <iostream>
/**
 * 1. 符号链接
 * 2.
 * @param s
 */
using namespace std;

void print_file_mode(struct stat sb);
void print_file_info(string name, struct stat  sb, int depth);
void printdir(string dir, int depth);
int add_len(char * a, char * b);
void concateStr(char *name, char *dir, char *child);
int dir_check(const char * dir);

int main(){
    char a[] = "/";
//    char a[] = "/home";
    printdir(a, 0);
    // print_dir("/home/martin/AllWorkStation/Clang/poj/1/1");
    return 0;
}

void printdir(string dir, int depth){

    if(depth >= 4){
        int i;
        i++;
    }


    DIR* dp;
    if((dp = opendir(dir.c_str())) == NULL){
        printf("GG\n");
        return;
    }

    struct dirent * clause;
    while(1){
        clause = readdir(dp);
        if(clause == NULL) break;
        struct stat sb;

        // concat the string
        string name = dir + "/" + clause->d_name;
        int check = lstat(name.c_str(), &sb);
        if(check == -1)continue;

        if(clause ->d_type == DT_DIR){
            // 检查是不是. 和 ..
            if(!dir_check(clause->d_name)){
                print_file_info(clause->d_name, sb, depth);
                printdir(name, depth + 1);
            }
        }else{
            print_file_info(name, sb, depth);
        }
    }

    closedir(dp);
}

int dir_check(const char * dir){
//    int len = 0;
//    while (dir[len] != 0){
//        len ++;
//    }
    string s(dir);
    if(s.compare(".") == 0) return 1;
    if(s.compare("..") == 0) return 1;
    return 0;
}



void print_file_info(string name, struct stat sb, int depth){
    printf("%d ", depth);
    print_file_mode(sb);
    struct passwd * a = getpwuid(sb.st_uid);
    struct group * b = getgrgid(sb.st_gid);
//    if(a == NULL || b == NULL) return;
    char time[17];
    // Www Mmm dd hh:mm:ss yyyy
    char * s = ctime(&sb.st_ctime);
    // Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec
    switch(s[4]){
        case 'F':
            time[5] = '0';
            time[6] = '2';
            break;
        case 'S':
            time[5] = '0';
            time[6] = '9';
            break;
        case 'O':
            time[5] = '1';
            time[6] = '0';
            break;
        case 'N':
            time[5] = '1';
            time[6] = '1';
            break;
        case 'D':
            time[5] = '1';
            time[6] = '2';
            break;
        case 'J':
            if(s[5] == 'a'){
                time[5] = '0';
                time[6] = '1';
            }else{
                if(s[6] == 'n'){
                    time[5] = '0';
                    time[6] = '5';
                }else{
                    time[5] = '0';
                    time[6] = '6';
                }
            }
            // Jan Jun Jul
            break;
        case 'M':
            // Mar May
            if(s[6] == 'r'){
                time[5] = '0';
                time[6] = '3';
            }else{
                time[5] = '0';
                time[6] = '5';
            }
            break;
        case 'A':
            // Apr aug
            if(s[6] == 'r'){
                time[5] = '0';
                time[6] = '4';
            }else{
                time[5] = '0';
                time[6] = '8';
            }
            break;
    }

    time[0] = s[20];
    time[1] = s[21];
    time[2] = s[22];
    time[3] = s[23];
    time[4] = '-';
    // time[5]
    // time[6]
    time[7] = '-';
    time[8] = s[8];
    time[9] = s[9];
    time[10] = '-';
    time[11] = s[11];
    time[12] = s[12];
    time[13] = s[13];
    time[14] = s[14];
    time[15] = s[15];
    time[16] = 0;


    printf(" %ld %s %s %lld %s ", (long) sb.st_nlink, a->pw_name, b->gr_name, (long long int)sb.st_size, time);
    cout << name << endl;

}

void print_file_mode(struct stat sb){
    printf( (sb.st_mode & S_IRUSR) ? "r" : "-");
    printf( (sb.st_mode & S_IWUSR) ? "w" : "-");
    printf( (sb.st_mode & S_IXUSR) ? "x" : "-");
    printf( (sb.st_mode & S_IRGRP) ? "r" : "-");
    printf( (sb.st_mode & S_IWGRP) ? "w" : "-");
    printf( (sb.st_mode & S_IXGRP) ? "x" : "-");
    printf( (sb.st_mode & S_IROTH) ? "r" : "-");
    printf( (sb.st_mode & S_IWOTH) ? "w" : "-");
    printf( (sb.st_mode & S_IXOTH) ? "x" : "-");
}
