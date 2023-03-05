# Deploy pgsql cluster on GKE
module "postgresql" {
  source       = "../modules"
  env          = var.env
  pgPass       = var.pgPass
  pgUser       = var.pgUser
  pgDb         = var.pgDb
}