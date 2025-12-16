# 0 - find all files
for f in <filenames>; do echo -n "-o -name \"$f\" "; done; echo 
find / <file-found> 2>/dev/null > found.txt

# 1 - file owen by best-group
for f in $(cat found.txt); do 
    if [ "$(stat -c %G $f)" = "best-group" ]; then
        echo $f;
    fi;
done


# 2 - files containing IP address
pattern='(\d{1,3}\.){3}\d{1,3}'
for f in $(cat found.txt); do
    if grep -qP "$pattern" "$f"; then
        echo $f;
    fi;
done

# 3 - File with defined hash
hash=<GIVEN-HASH>
for f in $(cat found.txt); do
    if [ "$(sha1sum $f | awk '{print $1}')" = $hash ]; then
        echo $f;
    fi;
done

# 4 - File containing 230 line
lines="<lines>"
for f in $(cat found.txt); do
    if [ "$(wc -l $f | awk '{print $1}')" = $lines ]; then
        echo $f;
    fi;
done

# 5 - File with given owner id
o_id="<GIVEN-UID>"
for f in $(cat found.txt); do
    if [ "$(stat -c %u $f)" = $o_id ]; then
        echo $f;
    fi;
done

# 6 - Executeable by everyone
for f in $(cat found.txt); do
    if [ -x $f ]; then
        echo $f;
    fi;
done