# aspnetcore/WildfireAPI$ docker build -f "Dockerfile" -t name:latest ../
# docker run --name cs_api -p 8080:8080 name:latest

ARG DOTNET_VERSION=9.0
ARG BUILD_CONFIGURATION=Release

FROM mcr.microsoft.com/dotnet/sdk:${DOTNET_VERSION} AS build
ENV ASPNETCORE_URLS=http://+:80

# WildfireAPI can only found if ../ in docker run
WORKDIR /src
COPY ["WildfireAPI/", "WildfireAPI/"]

WORKDIR /src/WildfireAPI
RUN dotnet restore "./WildfireAPI.csproj"
RUN dotnet build "./WildfireAPI.csproj" -c  "$BUILD_CONFIGURATION" -o /app/build
# runtime can be changed if necessary
RUN dotnet publish "./WildfireAPI.csproj" -c  "$BUILD_CONFIGURATION" -o /app/publish -r linux-musl-x64

FROM mcr.microsoft.com/dotnet/aspnet:${DOTNET_VERSION} AS run
WORKDIR /app
COPY --from=build /app/publish .
ENTRYPOINT [ "dotnet", "WildfireAPI.dll" ]