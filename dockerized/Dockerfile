# Use the official Windows Server Core image as the base image
FROM mcr.microsoft.com/windows/servercore:ltsc2019

# Set the PowerShell execution policy for the container
SHELL ["powershell", "-Command", "Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope CurrentUser -Force;"]

# Download FFmpeg from a trusted source and extract it
RUN Invoke-WebRequest -Uri 'https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-full.7z' -OutFile 'C:\ffmpeg.7z'; \
    Expand-Archive -Path 'C:\ffmpeg.7z' -DestinationPath 'C:\ffmpeg'; \
    Remove-Item -Path 'C:\ffmpeg.7z' -Force

# Set the PowerShell execution policy back to Restricted
SHELL ["powershell", "-Command", "Set-ExecutionPolicy -ExecutionPolicy Restricted -Scope CurrentUser -Force;"]

# Use the official Python image as the secondary base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the Python scripts and token.txt file into the container
COPY music_cog.py Main.py help_cog.py token.txt /app/

# Install necessary Python dependencies
RUN pip install discord.py youtube_dl

# Set the command to run your bot (replace YOUR_BOT_TOKEN with your actual bot token)
CMD ["python", "Main.py"]
