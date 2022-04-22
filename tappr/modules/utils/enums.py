from enum import Enum


class PRPATH(str, Enum):
    APPS_PLUGIN = "https://github.com/vmware-tanzu/apps-cli-plugin/pull/"
    SOURCE_CONTROLLER = "https://github.com/vmware-tanzu/source-controller/pull/"
    SERVICE_BINDINGS = "https://github.com/vmware-tanzu/servicebinding/pull/"
    SPRINT_BOOT_CONVENTION = "https://gitlab.eng.vmware.com/tap-conventions/spring-boot/spring-boot-conventions/-/merge_requests/"


class REGISTRY(str, Enum):
    GCR = "gcr"
    DOCKERHUB = "dockerhub"
    OTHER = "other"


class GITURL(str, Enum):
    GIT_SSH = "git@github.com"
    GIT_HTTPS = "https://github.com"
    GITLAB_VMWARE_SSH = "git@gitlab.eng.vmware.com"
    GITLAB_VMWARE_HTTPS = "https://gitlab.eng.vmware.com"
    OTHER = "other"


class PROJECT(str, Enum):
    APPS_PLUGIN = "apps-plugin"
    SOURCE_CONTROLLER = "source-controller"
    SERVICE_BINDINGS = "service-bindings"
    SPRINT_BOOT_CONVENTION = "sprint-boot-convention"


class OS(str, Enum):
    MAC = "darwin"
    LINUX = "linux"
    WIN = "windows"


class PROFILE(str, Enum):
    ITERATE_LOCAL = "iterate-local"
    ITERATE = "iterate"