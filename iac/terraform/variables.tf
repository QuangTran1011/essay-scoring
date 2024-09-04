variable "resource_group_location" {
  type        = string
  default     = "koreacentral"
  description = "Location of the resource group."
}

variable "node_count" {
  type        = number
  description = "The initial quantity of nodes for the node pool."
  default     = 1
}
