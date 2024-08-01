int countSeniors(char ** details, int detailsSize){
    int count = 0;
    int i = 0;
    for (; i < detailsSize; i++){
        char * detail = strdup(details[i]);
        char result[3];
        result[0] = detail[11];
        result[1] = detail[12];
        result[2] = '\0';
        printf("%s", result);
        int age = atoi(result);
        if (age > 60){
            count++;
        }
        free(detail);
    }
return count;
}