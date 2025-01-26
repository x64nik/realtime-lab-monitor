from fastapi import APIRouter
from pydantic import BaseModel
from ..utils.proxmox_api import proxmoxClient
import datetime

router = APIRouter()

@router.get("/status", tags=["lab"])
async def get_status():
    hypervisor = proxmoxClient.cluster.status.get()[0]
    qemus = proxmoxClient.nodes("alpha").qemu().get()
    
    running_vms = [qemu for qemu in qemus if qemu['status'] == "running"] 
    pfsense = proxmoxClient.nodes("alpha").qemu(101).status.current.get()['qmpstatus']
    haproxy = proxmoxClient.nodes("alpha").qemu(107).status.current.get()['qmpstatus']
    cloudflare_tunnels = proxmoxClient.nodes("alpha").qemu(102).status.current.get()['qmpstatus']
    nas = proxmoxClient.nodes("alpha").qemu(104).status.current.get()['qmpstatus']
    k3s = proxmoxClient.nodes("alpha").qemu(150).status.current.get()['qmpstatus']
            
    return [
    { 
        "title": "Hypervisor", 
        "status": "operational" if hypervisor['online'] == 1 else "issue", 
        "info": "Virtualization platform for managing multiple VMs." 
    },
    { 
        "title": "Nginx Gateway", 
        "status": "warning", 
        "info": "Reverse proxy and load balancer for web traffic, requires attention." 
    },
    { 
        "title": "HAProxy", 
        "status": "operational" if haproxy == "running" else "issue", 
        "info": "High-performance load balancer, operational if running." 
    },
    { 
        "title": "pfSense", 
        "status": "operational" if pfsense == "running" else "issue",
        "info": "Open-source firewall and router software." 
    },
    { 
        "title": "Cloudflare Tunnels", 
        "status": "operational" if cloudflare_tunnels == "running" else "issue", 
        "info": "Secure tunneling service connecting local services to Cloudflare." 
    },
    { 
        "title": "K3S Server", 
        "status": "operational" if k3s == "running" else "issue", 
        "info": "Lightweight Kubernetes for production workloads, operational if running." 
    },
    { 
        "title": "Custom Runners", 
        "status": "issue",
        "info": "Self-hosted runners for CI/CD workflows in GitHub Actions." 
    },
    { 
        "title": "TrueNAS", 
        "status": "operational" if nas == "running" else "issue", 
        "info": "FreeNAS-based storage server for managing and sharing files." 
    }
]
    
