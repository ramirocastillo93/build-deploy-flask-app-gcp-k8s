module "flask-app" {
  source = "../modules/flask-app"
  env    = var.env
}

module "gke_secret" {
  source              = "../modules/gke-secret"
  k8s_secret_name     = var.k8s_secret_name
  k8s_secret_password = var.k8s_secret_password
  k8s_secret_server   = var.k8s_secret_server
  k8s_secret_username = var.k8s_secret_username
}