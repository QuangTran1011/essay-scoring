terraform {
  required_version = ">=1.0"

  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~>3.0"
    }
  }
}

provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "rg" {
  location = var.resource_group_location
  name     = "ess-m1-group"
}

resource "azurerm_kubernetes_cluster" "k8s" {
  location            = azurerm_resource_group.rg.location
  name                = "m1-cluster"
  resource_group_name = azurerm_resource_group.rg.name
  dns_prefix          = "dns"
  identity {
    type = "SystemAssigned"
  }

  default_node_pool {
    name                = "agentpool"
    vm_size             = "Standard_E2ads_v5"
    node_count = 2   
    enable_node_public_ip = false
  }
}
