#include <stdio.h>
#include <stdlib.h>

int main() {
    char *line = NULL;
    size_t len = 0;
    size_t nread;
    
    printf("Welcome to the Echo Machine! (Press Ctrl+D to finish)\n");
    
    while (1) {
        printf("Please enter anything:\n");
        nread = getline(&line, &len, stdin);
        
        if (nread == -1) {
            // EOF reached (Ctrl+D pressed)
            break;
        }
        
        // Remove newline character if present
        if (nread > 0 && line[nread - 1] == '\n') {
            line[nread - 1] = '\0';
        }
        
        printf("You entered: %s\n\n", line);
    }
    
    // Free allocated memory before exiting
    free(line);
    
    return 0;
}
