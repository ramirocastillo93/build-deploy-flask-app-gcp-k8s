locals {
  namespace_name = "${var.namespace_name}-${var.env}"
}

resource "kubernetes_namespace" "example" {
  metadata {
    name = local.namespace_name
    annotations = {
      name = local.namespace_name
    }
  }
}

# resource "helm_release" "atlantis" {
#   name       = "atlantis-${var.env}"
#   repository = "file://./helm"
#   chart      = "./helm"
#   namespace  = "atlantis-${var.env}"
#   values = [
#     "${file("./helm/values/${var.env}.yaml")}"
#   ]
# }