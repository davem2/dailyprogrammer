#include <stdio.h>
#include <sys/stat.h>

static int fsize( char *fileName );
static void uuencode( char *fileName );

int main( int argc, char *argv[] )
{
    //printf("%s\n", argv[1]);
    uuencode(argv[1]);

    return 0;
}

void uuencode( char *fileName )
{
    struct stat fileStat;
    if(stat(fileName,&fileStat) < 0)
        return;

    printf("begin %o %s\n",fileStat.st_mode & (S_IRWXU|S_IRWXG|S_IRWXO),fileName);

    //printf("%d\n",fsize(f));

    long unencodedByteLen = fsize(fileName);
    long encodedByteLen = unencodedByteLen + (unencodedByteLen / 3.0);

    //printf("%d, %d\n", unencodedByteLen, encodedByteLen);

    int linecount = unencodedByteLen / 45;
    int lastlinelen = unencodedByteLen % 45;

    //printf("%d, %d\n", linecount, lastlinelen);

    FILE *f = fopen(fileName,"rb");
    unsigned char inbuf[3];
    unsigned char outbuf[4];
    for (int line = 0; line < linecount; line++)
    {
        printf("M");
        for (int i=0; i < 15; i++)
        {
            fread(inbuf,1,3,f);
            outbuf[0] = 32 + (inbuf[0] >> 2);
            outbuf[1] = 32 + (((inbuf[0] & 0x03) << 4) | (inbuf[1] >> 4) & 0x3f);
            outbuf[2] = 32 + (((inbuf[1] & 0x0f) << 2) | (inbuf[2] >> 6) & 0x3f);
            outbuf[3] = 32 + (inbuf[2] & 0x3f);
            //printf("0 %d (%c), %d (%c)\n",inbuf[0],inbuf[0],outbuf[0],outbuf[0]);
            //printf("1 %d (%c), %d (%c)\n",inbuf[1],inbuf[1],outbuf[1],outbuf[1]);
            //printf("2 %d (%c), %d (%c)\n",inbuf[2],inbuf[2],outbuf[2],outbuf[2]);
            //printf("3 -, %d (%c)\n",outbuf[3],outbuf[3]);
            printf("%c%c%c%c",outbuf[0],outbuf[1],outbuf[2],outbuf[3]);
        }
        printf("\n");
    }

    if(lastlinelen > 0)
    {
        printf("%c", ' ' + lastlinelen);
        inbuf[0] = 0;
        inbuf[1] = 0;
        inbuf[2] = 0;

        int count;
        while( count = fread(inbuf,1,3,f) )
        {
            if (count < 3) inbuf[2] = 0;
            if (count < 2) inbuf[1] = 0;

            outbuf[0] = 32 + (inbuf[0] >> 2);
            outbuf[1] = 32 + (((inbuf[0] & 0x03) << 4) | (inbuf[1] >> 4) & 0x3f);
            outbuf[2] = 32 + (((inbuf[1] & 0x0f) << 2) | (inbuf[2] >> 6) & 0x3f);
            outbuf[3] = 32 + (inbuf[2] & 0x3f);
            //printf("0 %d (%c), %d (%c)\n",inbuf[0],inbuf[0],outbuf[0],outbuf[0]);
            //printf("1 %d (%c), %d (%c)\n",inbuf[1],inbuf[1],outbuf[1],outbuf[1]);
            //printf("2 %d (%c), %d (%c)\n",inbuf[2],inbuf[2],outbuf[2],outbuf[2]);
            //printf("3 -, %d (%c)\n",outbuf[3],outbuf[3]);
            printf("%c%c%c%c",outbuf[0],outbuf[1],outbuf[2],outbuf[3]);
        }
        printf("\n");
    }

    printf("\nend\n");

    fclose(f);

    return;
}


int fsize( char *fileName )
{
    FILE *fp = fopen(fileName,"rb");

    fseek(fp, 0, SEEK_END); // seek to end of file
    int size = ftell(fp); // get current file pointer

    fclose(fp);

    return size;
}
