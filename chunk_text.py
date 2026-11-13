# Step 1: Read the extracted text

input_path = "data/extracted_text.txt"

with open(input_path, "r", encoding="utf-8") as file:
    text = file.read()


# Step 2: Define chunk size and overlap

chunk_size = 1000
overlap = 200


# Step 3: Create chunks

chunks = []

start = 0

while start < len(text):

    end = start + chunk_size

    chunk = text[start:end]

    chunks.append(chunk)

    start += chunk_size - overlap


# Step 4: Save the chunks

output_path = "data/chunks.txt"

with open(output_path, "w", encoding="utf-8") as file:

    for index, chunk in enumerate(chunks, start=1):

        file.write(f"\n\n========== CHUNK {index} ==========\n\n")
        file.write(chunk)


# Step 5: Display results

print("Text chunking completed successfully!")

print("Total characters:", len(text))

print("Total chunks created:", len(chunks))

print("\nFirst chunk preview:\n")
print(chunks[0])