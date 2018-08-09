#!/bin/bash
minikube start
minikube ssh "sudo sysctl -w vm.max_map_count=262144"
