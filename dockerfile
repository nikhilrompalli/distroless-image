FROM ubuntu AS build-env

FROM gcr.io/distroless/java:11
COPY --from=build-env /bin /bin
ADD . glibc-2.31.tar.gz
RUN tar -xvzf glibc-2.31.tar.gz
ADD /root/glibc-2.31 glibc-linuxthreads-2.3.6.tar.gz
WORKDIR /root/glibc-2.31
RUN tar -xvzf glibc-linuxthreads-2.3.6.tar.gz