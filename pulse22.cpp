#include <stdlib.h>
#include <stdio.h>
#include <ctype.h>
#include <string>
#ifndef _WINSOCK_DEPRECATED_NO_WARNINGS
#define _WINSOCK_DEPRECATED_NO_WARNINGS
#endif
#include "O22SIOMM.h"
#include "O22STRCT.h"

int main(int nArgs, char *pcharyArgs[])
{
        O22SnapIoMemMap objEpic;
        char *address = "127.0.0.1";
        const int modN = 0;
        const int ptN = 15;
        int nResult;

        // open a TCP connection
        nResult = objEpic.OpenEnet2(address, 2001, 10000, 1, SIOMM_TCP);
        if (nResult != SIOMM_OK) {
                printf("OpenEnet2 reports result %d, exiting.\n", nResult);
                exit(0);
        }

        // wait for the TCP connect to complete, not necessary for UDP
        usleep(100000);

        //      pulse the point 22 times:
        for(int i = 0; i < 22; i++) {
                nResult = objEpic.SetHDDigitalPointState(modN, ptN, 1);
                if (nResult != SIOMM_OK) {      // turn the point on
                        printf("Set digital point ON reports %d. Exiting.\n", nResult);
                        exit(0);
                }
                usleep(250000);
                nResult = objEpic.SetHDDigitalPointState(modN,ptN, 0);
                if (nResult != SIOMM_OK) {      // turn the point off
                        printf("Set digital point OFF reports %d. Exiting.\n", nResult);
                        exit(0);
                }
                usleep(250000);
        }

        return 0;
}
