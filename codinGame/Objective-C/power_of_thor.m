#import <Foundation/Foundation.h>

int main (int argc, const char * argv[]) {
    @autoreleasepool {
        int lx, ly, tx, ty;
        scanf("%d %d %d %d", &lx, &ly, &tx, &ty);
        while (true) {
            int t; // assuming we read t as the number of remaining turns
            scanf("%d", &t); // reading and ignoring it as per the original code
            int dx = (lx > tx) - (lx < tx);
            int dy = (ly > ty) - (ly < ty);
            tx += dx; ty += dy;

            NSMutableString *move = [NSMutableString string];
            if (dy > 0) [move appendString:@"S"];
            if (dy < 0) [move appendString:@"N"];
            if (dx > 0) [move appendString:@"E"];
            if (dx < 0) [move appendString:@"W"];
            
            printf("%s\n", [move UTF8String]);
        }
    }
    return 0;
}
