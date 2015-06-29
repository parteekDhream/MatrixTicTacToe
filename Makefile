CC=gcc
CFLAGS=-c -Wall

SOURCES:= $(shell find src/ -name '*.c')
HEADERS:= $(shell find src/ -name '*.h')
OBJECTS=$(SOURCES:.c=.o)
OBJ=maxtictoe_c

all: $(OBJ)

$(OBJ): $(OBJECTS)
	$(CC) $(OBJECTS) -o $(OBJ)

.o: $(SOURCES) $(HEADERS)
	$(CC) $(CFLAGS) $< -o $@

clean:
	rm -f src/*.o
	rm -f $(OBJ)